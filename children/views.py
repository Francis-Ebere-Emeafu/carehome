from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render, get_object_or_404
from django.utils import timezone
from datetime import datetime

from accounts.models import Account
from accounts.utils import is_manager
from children.models import Child, ChildRecord, StaffChildManager
from children.forms import ChildRegisterForm, ChildModifyForm, ChildRecordForm
from workbook.forms import (
        FoodForm,
        EmotionalWellbeingForm,
        HealthHygieneForm,
        EducationForm,
        ActivityForm,
        AchievementForm,
        AppointmentForm,
        KeyWorkForm,
        IncidentForm,
        )
from workbook.models import (
    Food,
    EmotionalWellbeing,
    HealthHygiene,
    Education,
    Activity,
    Achievement,
    Appointment,
    KeyWork,
    Incident,
)
from children.utils import get_time_constants

def register_child(request):
    if not is_manager(user=request.user):
        print("You are permitted")
        logout(request)
        return redirect('login')

    if request.method == 'POST':
        form = ChildRegisterForm(request.POST, request.FILES or None)
        if form.is_valid():

            form.save(commit=True)
            messages.success(request, "New child successfully registered")
            return redirect('children_list')
    else:
        form = ChildRegisterForm()
    return render(request, "children/register_child.html", {"form": form})


def children_list(request):
    children = Child.objects.all()
    context = {"children_list": children}
    return render(request, "children/children_list.html", context)


def modify_child_details(request, child_id=None):
    if not is_manager(user=request.user):
        print("You are permitted")
        logout(request)
        return redirect('login')

    child = get_object_or_404(Child, id=child_id)
    form = ChildModifyForm(request.POST or None, request.FILES or None, instance=child)
    if form.is_valid():
        updated = form.save()
        messages.success(request, "Child successfully updated")
        return redirect('children_list')
    context = {"child": child, "form": form}
    return render(request, "children/modify_child_details.html", context)


def enter_child_record(request):
    if request.method == "POST":
        form = ChildRecordForm(request.POST)
        if form.is_valid():
            pass
    return render(request, "children/enter_child_record.html")


def child_assignment_list(request):
    me = Account.objects.get(user=request.user)
    assigned_list = StaffChildManager.objects.filter(staff=me)
    children_list = Child.objects.filter(assigned=False)
    context = {"children_list": children_list, "assigned_list": assigned_list}
    return render(request, "children/child_assignment_list.html", context)


def my_child_selections(request):
    me = Account.objects.get(user=request.user)
    assigned_list = StaffChildManager.objects.filter(staff=me)
    context = {"assigned_list": assigned_list}
    return render(request, "children/my_child_selections.html", context)


def select_child(request, child_id):
    child = get_object_or_404(Child, id=child_id)
    me = Account.objects.get(user=request.user)
    StaffChildManager.objects.create(child=child, staff=me)
    child.assigned = True
    child.save()
    return redirect('child_assignment_list')


def child_record_list(request):
    me = Account.objects.get(user=request.user)
    children_list = StaffChildManager.objects.filter(staff=me)
    context = {"children_list": children_list}
    return render(request, "children/child_record_list.html", context)


def create_edit_child_record(request, child_id):
    child = Child.objects.get(id=child_id)
    day_of_week, daytime, greeting = get_time_constants()
    today = timezone.now()
    if daytime == "AM":
        day_time = 0
    else:
        day_time = 1

    child_record = ChildRecord.objects.filter(child=child, record_active=True).last()
    if not child_record:
        # No initial child's record, hence create a fresh record for the child
        child_record = ChildRecord.objects.create(child=child, date_created=today)
        child_record.emotional_wellbeing = EmotionalWellbeing.objects.create(daytime=day_time)
        child_record.health_hygiene = HealthHygiene.objects.create(daytime=day_time)
        child_record.education = Education.objects.create()
        child_record.activities = Activity.objects.create()
        child_record.achievements = Achievement.objects.create()
        child_record.appointments_contact = Appointment.objects.create()
        child_record.key_work = KeyWork.objects.create()
        child_record.incidents = Incident.objects.create()
        child_record.save()
    if today.date() > child_record.date_created.date():
        # confirm if the day is over and start a new child's record
        child_record.record_active = False
        child_record.save()
        record_instance = ChildRecord.objects.create(child=child, date_created=today)
        record_instance.emotional_wellbeing = EmotionalWellbeing.objects.create(daytime=day_time)
        record_instance.health_hygiene = HealthHygiene.objects.create(daytime=day_time)
        record_instance.education = Education.objects.create()
        record_instance.activities = Activity.objects.create()
        record_instance.achievements = Achievement.objects.create()
        record_instance.appointments_contact = Appointment.objects.create()
        record_instance.key_work = KeyWork.objects.create()
        record_instance.incidents = Incident.objects.create()
        record_instance.save()
    else:
        # Current record instance used for the record of the day.
        record_instance = child_record

    if not record_instance.emotional_wellbeing.daytime == day_time:
        record_instance.emotional_wellbeing = EmotionalWellbeing.objects.create(daytime=day_time)
        record_instance.save()
    if not record_instance.health_hygiene.daytime == day_time:
        record_instance.health_hygiene = HealthHygiene.objects.create(daytime=day_time)
        record_instance.save()

    # get record instance of all other related foriegnkey fields
    emotional_wellbeing_id = record_instance.emotional_wellbeing.id
    emotional_instance = EmotionalWellbeing.objects.get(pk=emotional_wellbeing_id)

    health_hygiene_id = record_instance.health_hygiene.id
    health_instance = HealthHygiene.objects.get(pk=health_hygiene_id)

    education_id = record_instance.education.id
    education_instance = Education.objects.get(pk=education_id)

    activities_id = record_instance.activities.id
    activities_instance = Activity.objects.get(pk=activities_id)

    achievements_id = record_instance.achievements.id
    achievements_instance = Achievement.objects.get(pk=achievements_id)

    appointments_id = record_instance.appointments_contact.id
    appointments_instance = Appointment.objects.get(pk=appointments_id)

    key_work_id = record_instance.key_work.id
    key_work_instance = KeyWork.objects.get(pk=key_work_id)

    incidents_id = record_instance.incidents.id
    incidents_instance = Incident.objects.get(pk=incidents_id)


    food_form = FoodForm(request.POST or None)
    emotional_form = EmotionalWellbeingForm(request.POST or None, instance=emotional_instance)
    health_form = HealthHygieneForm(request.POST or None, instance=health_instance)
    education_form = EducationForm(request.POST or None, instance=education_instance)
    activity_form = ActivityForm(request.POST or None, instance=activities_instance)
    achievement_form = AchievementForm(request.POST or None, instance=achievements_instance)
    appointment_form = AppointmentForm(request.POST or None, instance=appointments_instance)
    key_form = KeyWorkForm(request.POST or None, instance=key_work_instance)
    indident_form = IncidentForm(request.POST or None, instance=incidents_instance)

    form = ChildRecordForm(request.POST or None, request.FILES or None, instance=record_instance)
    if form.is_valid() and emotional_form.is_valid() and health_form.is_valid():
        child_record_update = form.save(commit=False)
        emotional_form.save()
        health_form.save()
        child_record_update.save()
        messages.success(request, "{}'s record successfully updated".format(child))
        return redirect('child_record_list')

    context = {
            "form": form,
            "child": child,
            "today": today,
            "greeting": greeting,
            "day_of_week": day_of_week,
            'food_form':food_form,
            'emotional_form':emotional_form,
            'health_form':health_form,
            'education_form':education_form,
            'activity_form':activity_form,
            'achievement_form':achievement_form,
            'appointment_form':appointment_form,
            'key_form':key_form,
            'indident_form':indident_form,
            }
    return render(request, "children/create_edit_child_record.html", context)


def create_record(request):
    if request.method == 'POST':
        form = EmotionalWellbeingForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('create_record')
    else:
        form = EmotionalWellbeingForm()
    return render(request, 'children/create_record.html', {"form": form})
