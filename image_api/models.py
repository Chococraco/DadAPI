from django.db import models

class Image(models.Model):
    latitude = models.FloatField(max_length=100)
    longitude = models.FloatField(max_length=100)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title
