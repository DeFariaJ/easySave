from django.db import models
from numpy import integer

# Create your models here.


class Users(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    age = models.IntegerField(blank=True, null=True)
    country = models.CharField(max_length=200, blank=True, null=True)
    email_field = models.EmailField(
        max_length=255, unique=True, blank=True, null=True)
