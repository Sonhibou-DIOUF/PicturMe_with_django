from django.db import models

class Client(models.Model):
    name = models.CharField(max_length=30,blank=True , null=True)
    email = models.EmailField(max_length=254, unique=True)
    phone_number = models.CharField(max_length=12)
    address = models.CharField(max_length=30, blank=True , null=True)

    def __str__(self):
        return self.name

