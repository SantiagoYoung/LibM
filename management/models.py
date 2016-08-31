from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class MySiteProfile(models.Model):
    user = models.ForeignKey(User, unique=True)

    favorate_band = models.CharField(max_length=100, blank=True)
    favorate_cheese = models.CharField(max_length=100, blank=True)
    lucky_number = models.IntegerField()

    def __str__(self):
        return self.user

class MyUser(models.Model):
    user = models.OneToOneField(User)
    nickname = models.CharField(max_length=16)
    permission = models.IntegerField(default=1)

    def __str__(self):
        return self.user.username

class Book(models.Model):
    name = models.CharField(max_length=128)
    price = models.FloatField()
    author = models.CharField(max_length=128)
    publish_date = models.DateTimeField()
    category = models.CharField(max_length=128)

    class META:
        ordering = ["name"]

    def __str__(self):
        return self.name

class Img(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField()
    img = models.ImageField(upload_to='image/')
    book = models.ForeignKey(Book)

    class META:
        ordering = ['name']

    def __str__(self):
        return self.name

