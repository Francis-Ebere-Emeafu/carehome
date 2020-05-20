from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render, get_object_or_404
from django.utils import timezone

from accounts.models import Account
from accounts.utils import is_manager
from children.models import Child, ChildRecord, StaffChildManager
from children.forms import ChildRegisterForm, ChildModifyForm, ChildRecordForm


def register_child(request):
    if not is_manager(user=request.user):
        print("You are permitted")
        logout(request)
        return redirect('login')

    if request.method == 'POST':
        form = ChildRegisterForm(request.POST)
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
    child_record = ChildRecord.objects.filter(child=child, record_active=True).last()
    today = timezone.now()

    if today.date() > child_record.date_created.date():
        child_record.record_active = False
        child_record.save()
        record_instance = ChildRecord.objects.create(child=child, date_created=today)
    else:
        record_instance = child_record

    form = ChildRecordForm(request.POST or None, request.FILES or None, instance=record_instance)
    if form.is_valid():
        form.save()
        messages.success(request, "{}'s record successfully updated".format(child))
        return redirect('child_record_list')

    context = {"form": form, "child": child, "today": today}
    return render(request, "children/create_edit_child_record.html", context)
