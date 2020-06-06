from django import forms
from django.urls import reverse

from crispy_forms.bootstrap import Field, InlineRadios, TabHolder, Tab
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Div, Fieldset

from dal import autocomplete


from accounts.models import Account
from workbook.models import (
    StaffTask,
    Food,
    EmotionalWellbeing,
    HealthHygiene,
    Education,
    Activity,
    Achievement,
    Appointment,
    KeyWork,
    Incident,
    )


YES = 0
NO = 1
ANSWER0 = enumerate(('Yes', 'No'))
ANSWER1 = enumerate(('Yes', 'No'))
ANSWER2 = enumerate(('Yes', 'No'))
ANSWER3 = enumerate(('Yes', 'No'))
ANSWER4 = enumerate(('Yes', 'No'))
ANSWER5 = enumerate(('Yes', 'No'))
ANSWER6 = enumerate(('Yes', 'No'))
ANSWER7 = enumerate(('Yes', 'No'))
ANSWER8 = enumerate(('Yes', 'No'))
ANSWER9 = enumerate(('Yes', 'No'))
ANSWER10 = enumerate(('Yes', 'No'))

AM = 0
PM = 1
DAYTIME0 = enumerate(('AM', 'PM'))
DAYTIME1 = enumerate(('AM', 'PM'))
DAYTIME2 = enumerate(('AM', 'PM'))
DAYTIME3 = enumerate(('AM', 'PM'))
DAYTIME4 = enumerate(('AM', 'PM'))

POSITIVE = 0
NEGATIVE = 1
MEASURE = enumerate(('Positive', 'Negative'))

LOW = 0
HIGH = 1
DEGREE = enumerate(('Low', 'High'))

BREAKFAST = 0
LUNCH = 1
DINNER = 2
SNACKS = 3
MEALTYPE = enumerate(('Breakfast', 'Lunch', 'Dinner', 'Snacks'))


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


class FoodForm(forms.ModelForm):
    # meal = forms.ChoiceField(choices=MEALTYPE, widget=forms.RadioSelect())
    mean = forms.ModelChoiceField(
        queryset=Food.objects.all(),
        widget=autocomplete.ModelSelect2(url='food_autocomplete')
    )
    class Meta:
        model = Food
        fields = ['meal', 'meal_type']


class EmotionalWellbeingForm(forms.ModelForm):
    daytime = forms.ChoiceField(choices=DAYTIME0, widget=forms.RadioSelect())
    measure = forms.ChoiceField(choices=MEASURE, widget=forms.RadioSelect())
    degree = forms.ChoiceField(choices=DEGREE, widget=forms.RadioSelect())

    class Meta:
        model = EmotionalWellbeing
        fields = ['daytime', 'measure', 'degree', 'comment',]

# diet_nutrition

class HealthHygieneForm(forms.ModelForm):
    daytime = forms.ChoiceField(choices=DAYTIME1, widget=forms.RadioSelect())
    medication_taken = forms.ChoiceField(choices=ANSWER0, widget=forms.RadioSelect())
    teeth_brushed = forms.ChoiceField(choices=ANSWER1, widget=forms.RadioSelect())
    bath_shower = forms.ChoiceField(choices=ANSWER2, widget=forms.RadioSelect())
    hair_washed = forms.ChoiceField(choices=ANSWER3, widget=forms.RadioSelect())
    # degree = forms.ChoiceField(choices=DEGREE, widget=forms.RadioSelect())

    class Meta:
        model = HealthHygiene
        fields = ['daytime', 'medication_taken', 'teeth_brushed',
        'bath_shower', 'hair_washed', 'diet_nutrition',]


class EducationForm(forms.ModelForm):
    homework_completed = forms.ChoiceField(choices=ANSWER4, widget=forms.RadioSelect())
    class Meta:
        model = Education
        fields = ['hours_attended', 'homework_completed',
                    'educational_activity', 'school_contact',]


class ActivityForm(forms.ModelForm):
    undertaken_activities = forms.ChoiceField(choices=ANSWER4, widget=forms.RadioSelect())
    class Meta:
        model = Activity
        fields = ['planned_activities', 'other_activities',
                    'undertaken_activities',]



class AchievementForm(forms.ModelForm):
    class Meta:
        model = Achievement
        fields = ['first', 'second', 'third',]


class AppointmentForm(forms.ModelForm):
    health_appointment = forms.ChoiceField(choices=ANSWER5, widget=forms.RadioSelect())
    professional_appointment = forms.ChoiceField(choices=ANSWER6, widget=forms.RadioSelect())
    contact_visit_call = forms.ChoiceField(choices=ANSWER7, widget=forms.RadioSelect())
    class Meta:
        model = Appointment
        fields = ['health_appointment', 'professional_appointment', 'contact_visit_call']



class KeyWorkForm(forms.ModelForm):
    requested_planned = forms.ChoiceField(choices=ANSWER8, widget=forms.RadioSelect())
    class Meta:
        model = KeyWork
        fields = ['requested_planned', 'topic']


class IncidentForm(forms.ModelForm):
    class Meta:
        model = Incident
        fields = ['title', 'consequence', 'intervention', 'comments']
