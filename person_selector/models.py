# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

from django.urls import reverse

class PersonSelector(models.Model):
    personid = models.AutoField(db_column='PersonId', primary_key=True)  # Field name made lowercase.
    firstname = models.CharField(db_column='FirstName', max_length=128)  # Field name made lowercase.
    lastname = models.CharField(db_column='LastName', max_length=128)  # Field name made lowercase.
    personcolour = models.CharField(db_column='PersonColour', max_length=128)  # Field name made lowercase.
    activeflag = models.BooleanField(db_column='ActiveFlag', blank=True, null=True)  # Field name made lowercase.
    dateselected = models.DateField(db_column='DateSelected', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'person_selector'

    def __str__(self):
        return f"{self.firstname} | {self.lastname} | {self.activeflag} | {self.dateselected}"

    # Keeping for learning purpose - this has been replaced by success_url in views.py
    # def get_absolute_url(self):
    #     return reverse('person_selector:get_person_selector_records') 


