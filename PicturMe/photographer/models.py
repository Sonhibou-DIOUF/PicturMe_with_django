from django.db import models
from event.models import EventModel
class Photographer(models.Model):
    name = models.CharField(max_length=255)
    specialty = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    phone = models.CharField(max_length=12)



    def __str__(self):
        return f'Photographer : {self.name}'