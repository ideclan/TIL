# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Theater(models.Model):
    id = models.IntegerField(blank=True, null=True)
    name = models.TextField(blank=True, null=True)
    location = models.TextField(blank=True, null=True)
    period = models.TextField(blank=True, null=True)
    place = models.TextField(blank=True, null=True)
    startdate = models.DateTimeField(blank=True, null=True)
    enddate = models.DateTimeField(blank=True, null=True)
    openrun = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'theater'


class TheaterDetails(models.Model):
    id = models.BigIntegerField(blank=True, null=True)
    age = models.TextField(blank=True, null=True)
    time = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    price = models.BigIntegerField(blank=True, null=True)
    shoptitle = models.TextField(db_column='shopTitle', blank=True, null=True)  # Field name made lowercase.
    shoplink = models.TextField(db_column='ShopLink', blank=True, null=True)  # Field name made lowercase.
    field_imglink = models.TextField(db_column=' imgLink', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it started with '_'.

    class Meta:
        managed = False
        db_table = 'theater_details'
