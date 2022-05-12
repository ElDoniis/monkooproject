from turtle import st
from django.db import models

# Create your models here.

class Events(models.Model):

    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255, null=True, blank=True)
    start = models.CharField(max_length=255, null=True, blank=True)
    end = models.CharField(max_length=255, null=True, blank=True)
    backgroundColor = models.CharField(max_length=255)
    borderColor = models.CharField(max_length=255)
    
    def __str__(self) -> str:
        return str(self.title) + str(self.start) + str(self.end) + str(self.backgroundColor) + str(self.borderColor)
