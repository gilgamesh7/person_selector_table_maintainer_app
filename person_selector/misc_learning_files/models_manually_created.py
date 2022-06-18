from django.db import models
from django.urls import reverse

# Create your models here.
class PersonSelector(models.Model):
    db_table = "person_selector"

    PersonId = models.IntegerField(primary_key=True)
    FirstName = models.CharField(max_length=128, blank=False)
    LastName = models.CharField(max_length=128, blank=True)
    ActiveFlag = models.BooleanField(default=True)
    DateSelected = models.DateTimeField(blank=True)

    def __str__(self):
        return f"{self.FirstName} | {self.LastName} | {self.ActiveFlag} | {self.DateSelected}"

    def get_absolute_url(self):
        return reverse('person_selector:get_person_selector_records')    