from django import forms

from accounts.models import Account
from workbook.models import StaffTask



class StaffTaskForm(forms.ModelForm):
    accounts = Account.objects.filter(user_type=Account.STAFF)
    staff = forms.ModelChoiceField(queryset=accounts, empty_label='Select Staff')
    class Meta:
        model = StaffTask
        fields = ['title', 'description', 'staff']
