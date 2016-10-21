from django.db import models

from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    followers = models.ManyToManyField('self', related_name='followees', symmetrical=False)

class Department(models.Model):
    name = models.CharField(max_length=100)

class Photo(models.Model):
    image = models.ImageField(upload_to="%Y/%m/%d")

class Employee(models.Model):
    author = models.ForeignKey(User, related_name='employees')
    department = models.ForeignKey(Department, related_name='department')
    photo = models.ForeignKey(Photo, related_name='photos', blank=True, null=True)
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)