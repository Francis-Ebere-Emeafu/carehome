from django import forms
from django.urls import reverse
from crispy_forms.bootstrap import Field, InlineRadios, TabHolder, Tab
from crispy_forms.helper import FormHelper

from crispy_forms.layout import Submit, Layout, Div, Fieldset


class PersonalDataForm(forms.Form):
   first_name = forms.CharField(required=True, max_length=255)
   last_name = forms.CharField(required=True, max_length=255)
   email = forms.EmailField(required=True)
   phone = forms.CharField(required=True, max_length=200)
   address = forms.CharField(max_length=1000, widget=forms.Textarea())
   more_info = forms.CharField(max_length=1000, widget=forms.Textarea())
   color = forms.TypedChoiceField(
       label="Choose color",
       choices=((0, "Red"), (1, "Blue"), (2, "Green")),
       coerce=lambda x: bool(int(x)),
       widget=forms.RadioSelect,
       initial='0',
       required=True)

   def __init__(self, *args, **kwargs):
       super(PersonalDataForm, self).__init__(*args, **kwargs)
       self.helper = FormHelper()
       self.helper.form_id = 'id-personal-data-form'
       self.helper.form_method = 'post'
       # self.helper.form_action = reverse('submit_form')
       self.helper.add_input(Submit('submit', 'Submit', css_class='btn-success'))
       self.helper.form_class = 'form-horizontal'
       self.helper.layout = Layout(
           Fieldset('Name',
                    Field('first_name', placeholder='Your first name',
                          css_class="some-class"),
                    Div('last_name', title="Your last name"),),
           Fieldset('Contact data', 'email', 'phone', style="color: brown;"),
           InlineRadios('color'),
           TabHolder(Tab('Address', 'address'),
                     Tab('More Info', 'more_info'))
           )
