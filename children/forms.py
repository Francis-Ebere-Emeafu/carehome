from django import forms
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User


from children.models import Child, ChildRecord, StaffChildManager
from accounts.models import Account
from workbook.models import StaffTask


class StaffTaskForm(forms.ModelForm):
    accounts = Account.objects.filter(user_type=Account.STAFF)
    staff = forms.ModelChoiceField(queryset=accounts, required=False, empty_label='Select Staff')
    class Meta:
        model = StaffTask
        fields = ['title', 'description', 'staff']


class AssignTaskForm(forms.ModelForm):
    accounts = Account.objects.filter(user_type=Account.STAFF)
    staff = forms.ModelChoiceField(queryset=accounts, required=False, empty_label='Select Staff')
    class Meta:
        model = StaffTask
        fields = ['staff']


class ChildRegisterForm(forms.ModelForm):
    # GENDER = enumerate(('Male', 'Female', 'Select'))
    # password = forms.CharField(max_length=100, widget=forms.PasswordInput, validators=[validate_password])
    # confirm = forms.CharField(max_length=100, widget=forms.PasswordInput)
    # gender = forms.ChoiceField(choices=GENDER, label='Select Gender')
    class Meta:
        model = Child
        fields = ['first_name', 'last_name', 'phone', 'email', 'gender']

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
                Child.objects.get(phone=phone)
                # ObjectDoesNotExist
            except ObjectDoesNotExist:
                try:
                    Account.objects.get(phone=phone)
                    # ObjectDoesNotExist
                except ObjectDoesNotExist:
                    return phone
                else:
                    raise forms.ValidationError("This phone number is in use!")


class ChildModifyForm(forms.ModelForm):
    class Meta:
        model = Child
        fields = ['first_name', 'last_name', 'phone', 'email', 'gender']


class ChildRecordForm(forms.ModelForm):
    class Meta:
        model = ChildRecord
        fields = ['feeding', 'medication', 'behaviour', 'notes', 'visit']


class StaffChildManagerForm(forms.ModelForm):
    children = Child.objects.filter(assigned=False)
    child = forms.ModelChoiceField(queryset=children, required=False, empty_label='Select Child')
    class Meta:
        model = StaffChildManager
        fields = ['child']
