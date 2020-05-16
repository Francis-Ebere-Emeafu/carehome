from django.shortcuts import redirect, render, get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
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
                return redirect('register')
            else:
                messages.warning(request, "You have entered an invalid username or password")
                return redirect('login')

    else:
        form = LoginForm()
    return render(request, 'accounts/login.html', {"form": form})


def logout_user(request):
    logout(request)
    return redirect('home')

#
# def profile(request):
#     context = {}
#     return render(request, 'accounts/profile.html', context)
# from django.shortcuts import render
#
# # Create your views here.
