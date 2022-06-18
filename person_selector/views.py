from re import L, template
from django.shortcuts import render
from django.views.generic import ListView

from person_selector.models import PersonSelector
from person_selector.forms import DisplayForm

# Create your views here.
class DisplayView(ListView):
    model = PersonSelector
    form_class = DisplayForm
    template_name = 'person_selector/get_person_records.html'

# def insert_person_selector_record(request):
#     return render(request,'person_selector/insert_person_record.html') 

# def update_person_selector_record(request):
#     return render(request,'person_selector/update_person_record.html')
