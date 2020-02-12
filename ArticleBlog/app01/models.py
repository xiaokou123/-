from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=32)
    date = models.DateField()
    content = models.TextField()
    description = models.TextField()
class type(models.Model):
    name = models.CharField(max_length=32)
    description = models.TextField()
class author(models.Model):
    name = models.CharField(max_length=32)
    gender = models.CharField(max_length=32)
    age = models.IntegerField()
    email = models.CharField(max_length=32)