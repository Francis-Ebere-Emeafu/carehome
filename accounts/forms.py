from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ObjectDoesNotExist

from accounts.models import Account
from accounts.utils import get_username_for_auth


class RegForm(forms.ModelForm):
    email = forms.EmailField()
    password = forms.CharField(
        max_length=100, widget=forms.PasswordInput, validators=[validate_password]
    )
    confirm = forms.CharField(max_length=100, widget=forms.PasswordInput)

    class Meta:
        model = Account
        fields = ['first_name', 'last_name', 'phone']

    def clean_email(self):
        if 'email' in self.cleaned_data:
            email = self.cleaned_data['email']
            try:
                User.objects.get(username=email)
            except User.DoesNotExist:
                return email
            else:
                raise forms.ValidationError("The email has already been used!")

    def clean_phone(self):
        if 'phone' in self.cleaned_data:
            phone = self.cleaned_data['phone']
            try:
                Account.objects.get(phone=phone)
                # ObjectDoesNotExist
            except ObjectDoesNotExist:
                return phone
            else:
                raise forms.ValidationError("This phone number is in use!")

    def clean(self):
        if "password" in self.cleaned_data and "confirm" in self.cleaned_data:
            if self.cleaned_data["password"] != self.cleaned_data["confirm"]:
                raise forms.ValidationError("The passwords do not match!")
            return self.cleaned_data


class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(max_length=100, widget=forms.PasswordInput)

    def clean(self):
        print('---------CLEANING THE DATA---------')
        if 'username' in self.cleaned_data and 'password' in self.cleaned_data:
            username = self.cleaned_data['username']
            password = self.cleaned_data['password']
            phone_email = get_username_for_auth(username)
            user = authenticate(username=phone_email, password=password)

            if user is not None:
                return self.cleaned_data
            elif user == "None":
                print('Raising Error')
                raise forms.ValidationError('Wrong username or password')
            # if user is None:
            #     raise forms.ValidationError('Wrong username or password')
            # return self.cleaned_data
