from django.urls import path

from person_selector import views

urlpatterns = [
    path('', views.get_person_selector_records , name='get_person_selector_records'),
    path('insert/', views.insert_person_selector_record , name='insert_person_selector_record'),
    path('update/', views.update_person_selector_record , name='update_person_selector_record'),
]
