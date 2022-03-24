from django.db import models

# Create your models here.

class Events(models.Model):

    even_id = models.AutoField(primary_key=True)
    event_name = models.CharField(max_length=255, null=True, blank=True)
    start_date = models.DateTimeField(null=True, blank=True)
    end_date = models.DateTimeField(null=True, blank=True)
    background_color = models.CharField(max_length=255)
    border_color = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.event_name