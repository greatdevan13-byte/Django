from django.db import models

# Create your models here.
class library(models.Model):
    book_title=models.CharField(max_length=50)
    authors_name=models.CharField(max_length=50)