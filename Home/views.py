from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import auth
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from Home.models import Farmer, Buyer
from Home.forms import FarmerRegistrationForm, BuyerRegistrationForm, PortalLoginForm
from Home.utils import is_farmer, is_buyer


#Here Logic of data base Registration to user input
def FarmerRegistrationPage(request):
    if request.method == 'POST':
        form = FarmerRegistrationForm(request.POST)
        if form.is_valid():
            password = form.cleaned_data['password']
            username = form.cleaned_data['email']

            new_user =User.objects.create_user(username=username, email=username, password=password)
            new_user.save()

            farmer = form.save(commit=False)
            farmer.user = new_user
            farmer.save()
            return redirect('portal_login')
    else:
        form = FarmerRegistrationForm()
    return render(request, "RegistrationFormFarmer.html", {"form": form})


def BuyerRegistrationPage(request):
    if request.method == 'POST':
        form = BuyerRegistrationForm(request.POST)
        if form.is_valid():
            password = form.cleaned_data['password']
            username = form.cleaned_data['email']

            new_user =User.objects.create_user(username=username, email=username, password=password)
            new_user.save()

            buyer = form.save(commit=False)
            buyer.user = new_user
            buyer.save()
            return redirect('portal_login')
    else:
        form = BuyerRegistrationForm()
    return render(request, "RegistrationFormBuyer.html", {"form": form})


def PortalLogin(request):
    if request.method == 'POST':
        form = PortalLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]

            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('portal_profile')
            else:
                messages.warning(request, "You have entered an invalid username or password")
                return redirect('portal_login')
    else:
        form = PortalLoginForm()
    return render(request, 'PortalFormLogin.html', {"form": form})


def PortalLogout(request):
    logout(request)
    return redirect('/')



def PortalProfile(request):
    print('confirm profile type')
    if is_farmer(request.user):
        print('this is a farmer')
        return redirect('farmer_profile')
    elif is_buyer(request.user):
        print('this is a buyer')
        return redirect('buyer_profile')
    else:
        return redirect('/')


def FarmerProfile(request):
    farmer = Farmer.objects.get(user=request.user)
    return render(request,'FarmerPorfile.html', {"farmer": farmer})


def BuyerProfile(request):
    buyer = Buyer.objects.get(user=request.user)
    return render(request,'BuyerProfile.html', {"buyer": buyer})


def SellForm(request):
    return render(request,'SellForm.html')

def BuyForm(request):
    return render(request,'BuyForm.html')
# Create your views here.
def HomePage(request):
    return render(request,'MainIndex.html')

def ServicesUS(request):
    return render(request,'Services.html')

def searchProduces(request):
    return render(request,'SearchProduces.html')

def HelpUS(request):
    return render(request,'Help.html')

def ContactUS(request):
    return render(request,'Contact.html')

def AboutUS(request):
    return render(request,'About.html')
