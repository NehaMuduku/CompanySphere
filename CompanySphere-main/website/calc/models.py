# models.py
from django.db import models

class User(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
from djongo import models

class Microsoft(models.Model):
    introduction = models.CharField(max_length=500)
    about = models.TextField()
    recent1 = models.TextField()
    recent2 = models.TextField()
    recent3 = models.TextField()
    recent4 = models.TextField()


# models.py

from django.db import models

class FreshersData(models.Model):
    year1 = models.IntegerField()
    year2 = models.IntegerField()
    year3 = models.IntegerField()
    number_of_freshers1 = models.IntegerField()
    number_of_freshers2 = models.IntegerField()
    number_of_freshers3 = models.IntegerField()

    

class YourModel(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
# models.py
