from django.shortcuts import redirect, render, get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from accounts.models import Account

from accounts.forms import RegForm, LoginForm
from accounts.utils import get_username_for_auth


def register(request):
    if request.method == 'POST':
        form = RegForm(request.POST)
        if form.is_valid():
            password = form.cleaned_data['password']
            username = form.cleaned_data['email']

            new_user =User.objects.create_user(username=username, email=username, password=password)
            new_user.save()

            account = form.save(commit=False)
            account.user = new_user
            account.email = username
            account.save()
    else:
        form = RegForm()
    return render(request, "accounts/register.html", {"form": form})


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




def staff_profile(request):
    account = Account.objects.get(user=request.user)
    context = {"account": account}
    return render(request, 'accounts/staff.html', context)


def senior_staff_profile(request):
    account = Account.objects.get(user=request.user)
    context = {"account": account}
    return render(request, 'accounts/senior_staff.html', context)


def manager_profile(request):
    account = Account.objects.get(user=request.user)
    context = {"account": account}
    return render(request, 'accounts/manager.html', context)


def profile(request):
    account = Account.objects.get(user=request.user)
    context = {"account": account}
    return render(request, 'accounts/profile.html', context)
