from re import L, template
from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from person_selector.models import PersonSelector
from person_selector.forms import DisplayForm, CreateForm, UpdateForm

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

class UpdateView(UpdateView):
    model = PersonSelector
    form_class = UpdateForm
    template_name = 'person_selector/update_person_record.html'   

    success_url = reverse_lazy('person_selector:get_person_selector_records')


class DeleteView(DeleteView):
    model = PersonSelector
    template_name = 'person_selector/delete_person_record.html'   

    success_url = reverse_lazy('person_selector:get_person_selector_records')
