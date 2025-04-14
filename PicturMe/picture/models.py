from django.db import models

class PictureModel(models.Model):
    class PhotoModel(models.Model):
        picture_id = models.IntegerField(primary_key=True)
        file_path = models.CharField(max_length=1000)
        resolution = models.CharField(max_length=60)
        file_format = models.CharField(max_length=300)
