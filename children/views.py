from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render, get_object_or_404

from accounts.models import Account
from accounts.utils import is_manager
from children.models import Child, ChildRecord, StaffChildManager
from children.forms import ChildRegisterForm, ChildModifyForm


def register_child(request):
    if not is_manager(user=request.user):
        print("You are permitted")
        logout(request)
        return redirect('login')

    if request.method == 'POST':
        form = ChildRegisterForm(request.POST)
        if form.is_valid():
            # password = form.cleaned_data['password']
            # username = form.cleaned_data['email']
            # new_user =User.objects.create_user(username=username, email=username, password=password)
            # new_user.save()
            # account = form.save(commit=False)
            # account.user = new_user
            # account.email = username
            # account.save()
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


def select_child(request, child_id):
    child = get_object_or_404(Child, id=child_id)
    me = Account.objects.get(user=request.user)
    StaffChildManager.objects.create(child=child, staff=me)
    child.assigned = True
    child.save()
    return redirect('child_assignment_list')
