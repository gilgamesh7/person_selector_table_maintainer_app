from django import forms
from person_selector.models import PersonSelector

class DisplayForm(forms.ModelForm):
    class Meta:
        model = PersonSelector
        fields = ('PersonId', 'FirstName', 'LastName', 'ActiveFlag', 'DateSelected')

        widgets = {
            'PersonId' : forms.IntegerField(),
            'FirstName' : forms.TextInput(attrs={'class': 'form-control','placeholder':'This is a placeholder'}),
            'LastName' : forms.TextInput(attrs={'class': 'form-control','placeholder':'This is a placeholder'}),
            'ActiveFlag' : forms.BooleanField(),
            'DateSelected' : forms.DateField(),
        }