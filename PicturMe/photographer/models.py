from django.db import models
from event.models import EventModel
class PhotographerModel(models.Model):
    photographer_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)
    specialty = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    phone = models.CharField(max_length=30)