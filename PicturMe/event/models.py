from django.db import models
from client.models import Client
from photographer.models import Photographer
from picture.models import Picture
from transaction.models import Transaction



class Event(models.Model):
    photographer = models.ForeignKey(Photographer, on_delete=models.CASCADE)
    picture = models.ForeignKey(Picture, on_delete=models.CASCADE)
    transaction = models.ForeignKey(Transaction, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    session_date = models.DateField()
    session_time = models.DateTimeField()
    location = models.CharField(max_length=300)


    def __str__(self):
        return f'{self.photographer}--{self.client}'