from django.db import models


class Question(models.Model):
    latitude = models.FloatField(max_length=100)
    longitue = models.FloatField(max_length=100)
    image = models.CharField(max_length=200)