from django.urls import path

from person_selector.views import DisplayView, InsertView

app_name = "person_selector"

urlpatterns = [
    path('', DisplayView.as_view() , name='get_person_selector_records'),
    path('insert/', InsertView.as_view() , name='insert_person_selector_record'),
    # path('update/', views.update_person_selector_record , name='update_person_selector_record'),
]
