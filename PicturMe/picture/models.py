from django.db import models

class Picture(models.Model):
    FILE_FORMAT_CHOICES = [
        ('jpg', 'JPEG'),
        ('png', 'PNG'),
        ('jpeg', 'JPEG'),
        ('gif', 'GIF'),
        ('tiff', 'TIFF'),
    ]
    picture_file = models.ImageField(upload_to='pictures', null=True, blank=True)
    resolution = models.CharField(max_length=60, null=True, blank=True)
    file_format = models.CharField(
        max_length=255,
        choices= FILE_FORMAT_CHOICES,
        null=True,
        blank=True
    )

    def __str__(self):
        return self.picture_file.name
