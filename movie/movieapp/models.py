from django.db import models

# Create your models here.
class Movie(models.Model):
    moviename=models.CharField(max_length=50)
    year=models.IntegerField()
