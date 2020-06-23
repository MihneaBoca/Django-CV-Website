from django.db import models


# Create your models here.

class CV(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=15)
    address = models.CharField(max_length=20)
    pers_desc = models.TextField(default='')
    experience = models.TextField(default='')
    education = models.TextField(default='')
    skills = models.TextField(default='')
    hobbies = models.TextField(default='')
