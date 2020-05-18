from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ObjectDoesNotExist

from Home.models import Farmer, Buyer


class FarmerRegistrationForm(forms.ModelForm):
    password = forms.CharField(max_length=100, widget=forms.PasswordInput, validators=[validate_password])
    confirm_password = forms.CharField(max_length=100, widget=forms.PasswordInput)

    class Meta:
        model = Farmer
        fields = ['first_name', 'last_name', 'email', 'occupation', 'phone_number', 'address', 'state']

    def clean_email(self):
        if 'email' in self.cleaned_data:
            email = self.cleaned_data['email']
            try:
                User.objects.get(username=email)
            except User.DoesNotExist:
                return email
            else:
                raise forms.ValidationError("The email has already been used!")

    def clean(self):
        if "password" in self.cleaned_data and "confirm_password" in self.cleaned_data:
            if self.cleaned_data["password"] != self.cleaned_data["confirm_password"]:
                raise forms.ValidationError("The passwords do not match!")
            return self.cleaned_data


class BuyerRegistrationForm(forms.ModelForm):
    password = forms.CharField(max_length=100, widget=forms.PasswordInput, validators=[validate_password])
    confirm_password = forms.CharField(max_length=100, widget=forms.PasswordInput)

    class Meta:
        model = Buyer
        fields = ['first_name', 'last_name', 'email', 'occupation', 'phone_number', 'address', 'state']

    def clean_email(self):
        if 'email' in self.cleaned_data:
            email = self.cleaned_data['email']
            try:
                User.objects.get(username=email)
            except User.DoesNotExist:
                return email
            else:
                raise forms.ValidationError("The email has already been used!")

    def clean(self):
        if "password" in self.cleaned_data and "confirm_password" in self.cleaned_data:
            if self.cleaned_data["password"] != self.cleaned_data["confirm_password"]:
                raise forms.ValidationError("The passwords do not match!")
            return self.cleaned_data



class PortalLoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(max_length=100, widget=forms.PasswordInput)

    def clean(self):
        if 'username' in self.cleaned_data and 'password' in self.cleaned_data:
            username = self.cleaned_data['username']
            password = self.cleaned_data['password']
            user = authenticate(username=username, password=password)

            if user is not None:
                return self.cleaned_data
            elif user == "None":
                raise forms.ValidationError('Wrong username or password')
            # if user is None:
            #     raise forms.ValidationError('Wrong username or password')
            # return self.cleaned_data
