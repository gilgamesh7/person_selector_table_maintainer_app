from django.urls import path

from person_selector.views import DisplayView, InsertView, UpdateView, DeleteView

app_name = "person_selector"

urlpatterns = [
    path('', DisplayView.as_view() , name='get_person_selector_records'),
    path('insert/', InsertView.as_view() , name='insert_person_selector_record'),
    path('update/<int:pk>', UpdateView.as_view() , name='update_person_selector_record'),
    path('delete/<int:pk>', DeleteView.as_view() , name='delete_person_selector_record'),
]
