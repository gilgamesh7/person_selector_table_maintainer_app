from re import L, template
from django.shortcuts import render
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy

from person_selector.models import PersonSelector
from person_selector.forms import DisplayForm, CreateForm

# Create your views here.
class DisplayView(ListView):
    model = PersonSelector
    form_class = DisplayForm
    template_name = 'person_selector/get_person_records.html'

class InsertView(CreateView):
    model = PersonSelector
    form_class = CreateForm
    template_name = 'person_selector/insert_person_record.html'   
    # Keeping this for learning purposes - you can use fields list if NOT using form_class
    # fields = ['firstname','lastname','activeflag']

    success_url = reverse_lazy('person_selector:get_person_selector_records')


# def update_person_selector_record(request):
#     return render(request,'person_selector/update_person_record.html')
