from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import redirect, render, get_object_or_404

from accounts.models import Account
from children.models import Child, ChildRecord, StaffChildManager

from accounts.forms import RegForm, LoginForm, ModifyForm
from accounts.utils import get_username_for_auth, is_manager


def register_staff(request):
    if not is_manager(user=request.user):
        print("You are permitted")
        logout(request)
        return redirect('login')

    if request.method == 'POST':
        form = RegForm(request.POST, request.FILES or None)
        if form.is_valid():
            password = form.cleaned_data['password']
            username = form.cleaned_data['email']

            new_user =User.objects.create_user(username=username, email=username, password=password)
            new_user.save()

            account = form.save(commit=False)
            account.user = new_user
            account.email = username
            account.save()
            messages.success(request, "New Staff successfully registered")
            return redirect('register_staff')
    else:
        form = RegForm()
    return render(request, "accounts/register_staff.html", {"form": form})


def staff_management_list(request):
    me = request.user
    accounts = Account.objects.all().exclude(user=me)
    context = {"staff_list": accounts}
    return render(request, "accounts/staff_management_list.html", context)


def modify_staff(request, profile_id=None):
    if not is_manager(user=request.user):
        print("You are permitted")
        logout(request)
        return redirect('login')
    staff = get_object_or_404(Account, id=profile_id)
    form = ModifyForm(request.POST or None, request.FILES or None, instance = staff)
    if form.is_valid():
        staff_update = form.save()
        messages.success(request, "Successfully Edited")
        return redirect('staff_management_list')
    context = {"staff": staff, "form": form}
    return render(request, "accounts/modify_staff.html", context)


def login_user(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]

            phone_email = get_username_for_auth(username)
            user = authenticate(username=phone_email, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.warning(request, "You have entered an invalid username or password")
                return redirect('login')
    else:
        form = LoginForm()
    return render(request, 'accounts/login.html', {"form": form})


def logout_user(request):
    logout(request)
    return redirect('login')


def confirm_delete_staff(request, profile_id):
    if not is_manager(user=request.user):
        print("You are permitted")
        logout(request)
        return redirect('login')
    account = get_object_or_404(Account, id=profile_id)
    username = account.user.username
    user_instance = User.objects.get(username=username)
    # if user_instance is not None:
    #     print(user_instance)
    #     user_instance.delete()
    #     return redirect("staff_management_list")
    account.delete()
    messages.success(request, "{} Account was successfully deleted".format(account))
    return redirect('staff_management_list')


def delete_staff(request, profile_id):
    if not is_manager(user=request.user):
        print("You are permitted")
        logout(request)
        return redirect('login')
    staff = get_object_or_404(Account, id=profile_id)
    return render(request, 'accounts/delete_staff.html', {"staff": staff})


def staff_profile(request):
    account = Account.objects.get(user=request.user)
    assigned_list = StaffChildManager.objects.filter(staff=account)
    children_list = Child.objects.filter(assigned=False)
    context = {"account": account, "children_list": children_list, "assigned_list": assigned_list}
    return render(request, 'accounts/staff.html', context)


def senior_staff_profile(request):
    account = Account.objects.get(user=request.user)
    context = {"account": account}
    return render(request, 'accounts/senior_staff.html', context)


def manager_profile(request):
    account = Account.objects.get(user=request.user)
    context = {"account": account}
    return render(request, 'accounts/manager.html', context)


def create_super_user_profile(request):
    # This function creates temporary user Account profile
    account = Account.objects.create(
        user=request.user,
        user_type = Account.MANAGER,
        first_name = 'Super',
        last_name = 'Account',
        phone = 'phone_email',
        email = request.user.email)
    return redirect('home')
