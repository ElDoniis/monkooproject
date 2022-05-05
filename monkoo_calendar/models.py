import json
from multiprocessing import Event
from django.db import models

# Create your models here.

class Events(models.Model):

    event_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255, null=True, blank=True)
    start = models.CharField(max_length=255, null=True, blank=True)
    end = models.CharField(max_length=255, null=True, blank=True)
    backgroundColor = models.CharField(max_length=255)
    borderColor = models.CharField(max_length=255)

    def __str__(self):
        return str(self.event_name)
        #return str(self.even_id) + " " +str(self.event_name) + " " + str(self.start_date) + " " +str(self.end_date) + " " +str(self.background_color) + " " + str(self.border_color)

def queryset_to_list(qs, fields=None, exclude=None):
    my_list=[]
    for x in qs:
        my_list.append(Events(x, fields, exclude))
    return my_list  
