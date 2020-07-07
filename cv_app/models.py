from django.db import models


# Create your models here.

class CV(models.Model):
    username = models.CharField(max_length=20, unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=20)
    phone_number = models.TextField(default='')
    address = models.TextField(default='')
    pers_desc = models.TextField(default='')
    experience = models.TextField(default='')
    education = models.TextField(default='')
    skills = models.TextField(default='')
    hobbies = models.TextField(default='')
