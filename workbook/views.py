from django.shortcuts import redirect, render, get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

from dal import autocomplete

from workbook.models import StaffTask, Task, Food
from workbook.forms import StaffTaskForm, AssignTaskForm
from accounts.models import Account
from accounts.utils import get_username_for_auth, is_manager


def create_task(request):
    if not is_manager(user=request.user):
        print("You are permitted")
        logout(request)
        return redirect('login')

    if request.method == 'POST':
        form = StaffTaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.save()
            return redirect('manage_all_task')
    else:
        form = StaffTaskForm()
    return render(request, "workbook/create_task.html", {"form": form})


def manage_all_task(request):
    staff = Account.objects.filter(user_type=Account.STAFF)
    tasks = StaffTask.objects.all()
    context = {"staff_list": staff, "tasks": tasks}
    return render(request, "workbook/manage_all_task.html", context)


def completed_task(request):
    staff = Account.objects.filter(user_type=Account.STAFF)
    tasks = StaffTask.objects.filter(completed=True)
    context = {"staff_list": staff, "tasks": tasks}
    return render(request, "workbook/completed_task.html", context)


def incompleted_task(request):
    staff = Account.objects.filter(user_type=Account.STAFF)
    tasks = StaffTask.objects.filter(completed=False)
    context = {"staff_list": staff, "tasks": tasks}
    return render(request, "workbook/incompleted_task.html", context)


def edit_task(request, task_id=None):
    if not is_manager(user=request.user):
        print("You are permitted")
        logout(request)
        return redirect('login')

    task = get_object_or_404(StaffTask, id=task_id)
    form = StaffTaskForm(request.POST or None, request.FILES or None, instance=task)
    if form.is_valid():
        task_update = form.save()
        messages.success(request, "Task successfully updated")
        return redirect('manage_all_task')
    context = {"task": task, "form": form}
    return render(request, "workbook/edit_task.html", context)


def assign_task_list(request):
    form = AssignTaskForm()
    tasks = StaffTask.objects.filter(completed=False)
    context = {"tasks": tasks, "form": form}
    return render(request, "workbook/assign_task_list.html", context)


def assign_task(request, task_id, staff_id):
    task = StaffTask.objects.get(id=task_id)
    staff = Account.objects.get(id=staff_id)
    task.staff = staff
    task.save()
    return redirect('')


def delete_task(request, task_id):
    if not is_manager(user=request.user):
        print("You are permitted")
        logout(request)
        return redirect('login')
    task = get_object_or_404(StaffTask, id=task_id)
    return render(request, 'workbook/delete_task.html', {"task": task})


def confirm_delete_task(request, task_id):
    if not is_manager(user=request.user):
        print("You are permitted")
        logout(request)
        return redirect('login')
    task = get_object_or_404(StaffTask, id=task_id)
    task.delete()
    messages.success(request, "{} Task was successfully deleted".format(task))
    return redirect('manage_all_task')


def staff_task_list(request):
    account = Account.objects.get(user=request.user)
    task_list = StaffTask.objects.filter(staff=account)
    context = {"task_list": task_list}
    return render(request, "workbook/staff_task_list.html", context)


def staff_complted_tasks(request):
    account = Account.objects.get(user=request.user)
    completed_task_list = StaffTask.objects.filter(staff=account, completed=True)
    context = {"completed_task_list": completed_task_list}
    return render(request, "workbook/staff_complted_tasks.html", context)


class FoodAutocomp(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = Food.objects.all()
        if self.q:
            qs = qs.filter(name__istartswith=self.q)
        return qs
