from django.db import models
from django.contrib.auth.models import User
from bitfield import BitField
from django_filters import rest_framework as filters

class Colors(models.Model):
    color = models.CharField(db_column='Color', max_length=30, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'colors'

class Types(models.Model):
    type = models.CharField(db_column='Type', max_length=30, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'types'

class Tasks(models.Model):
    tname = models.CharField(db_column='TName', max_length=30, blank=True, null=False)
    descr = models.CharField(db_column='Descr', max_length=255, blank=True, null=True)
    dateTask = models.DateTimeField(db_column='DateTask')  # Field name made lowercase.
    datenotif = models.DateTimeField(db_column='DateNotif')  # Field name made lowercase.
    color = models.ForeignKey(Colors, on_delete = models.CASCADE)
    reminder = models.BooleanField(db_column='Reminder')  # Field name made lowercase. This field type is a guess.
    type = models.ForeignKey(Types, models.DO_NOTHING, db_column='Type_id')  # Field name made lowercase.
    flag = models.BooleanField(db_column='Flag')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    class Meta:
        managed = True
        db_table = 'tasks'

class CharFilterInFilter(filters.BaseInFilter, filters.CharFilter):
    pass
class TasksFilter(filters.FilterSet):
    tname = CharFilterInFilter(field_name='tname', lookup_expr='in')
    dateTask = filters.RangeFilter()

    class Meta:
        model: Tasks
        fields = ['dateTask', 'tname']

class AddError(models.Model):
    flag = models.BooleanField()
   

    class Meta:
        ordering = ['flag']

# Create your models here.s
