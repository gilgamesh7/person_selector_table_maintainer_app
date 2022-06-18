from django.shortcuts import render

# Create your views here.
def get_person_selector_records(request):
    return render(request,'person_selector/get_person_records.html')

def insert_person_selector_record(request):
    return render(request,'person_selector/insert_person_record.html') 

def update_person_selector_record(request):
    return render(request,'person_selector/update_person_record.html')
