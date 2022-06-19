from django import forms
from person_selector.models import PersonSelector

class DisplayForm(forms.ModelForm):
    class Meta:
        model = PersonSelector
        fields = ('personid', 'firstname', 'lastname', 'activeflag', 'dateselected')

        widgets = {
            'personid' : forms.IntegerField(),
            'firstname' : forms.TextInput(attrs={'class': 'form-control','placeholder':'This is a placeholder'}),
            'lastname' : forms.TextInput(attrs={'class': 'form-control','placeholder':'This is a placeholder'}),
            'activeflag' : forms.BooleanField(),
            'dateselected' : forms.DateField(),
        }

class CreateForm(forms.ModelForm):
    class Meta:
        model = PersonSelector
        fields = ('firstname', 'lastname', 'activeflag')

        widgets = {
            'firstname' : forms.TextInput(attrs={'class': 'form-control','placeholder':'This is a placeholder'}),
            'lastname' : forms.TextInput(attrs={'class': 'form-control','placeholder':'This is a placeholder'}),
            # Keeping this for learning purpose - "'BooleanField' object has no attribute 'is_hidden'"
            # This is because BooleanField is a form_fieldand not a widget
            # 'activeflag' : forms.BooleanField(),
        }

class UpdateForm(forms.ModelForm):
    class Meta:
        model = PersonSelector
        fields = ('firstname', 'lastname', 'activeflag', 'dateselected')

        widgets = {
            'firstname' : forms.TextInput(attrs={'class': 'form-control','placeholder':'Enter First Name'}),
            'lastname' : forms.TextInput(attrs={'class': 'form-control','placeholder':'Enter Last Name'}),
            'dateselected': forms.DateInput(format=('%Y-%m-%d'),attrs={'class': 'form-control', 'placeholder': 'Select a date','type': 'date'}),
        }