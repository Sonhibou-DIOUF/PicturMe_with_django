from django.db import models
class EventModel(models.Model):
    event_id = models.IntegerField(primary_key=True)
    session_date = models.DateField()
    session_time = models.DateTimeField()
    location = models.CharField(max_length=300)