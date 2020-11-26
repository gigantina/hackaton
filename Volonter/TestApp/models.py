from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser


class Event(models.Model):
    id = models.AutoField(primary_key=True)
    startDate = models.CharField(max_length=20)
    endDate = models.CharField(max_length=20)
    title = models.CharField(max_length=25)
    description = models.CharField(max_length=200)
    long_description = models.TextField(null=True)
    img = models.ImageField(blank=True, upload_to='images/')
    address = models.TextField()


class Donate(models.Model):
    id = models.AutoField(primary_key=True)
    startDate = models.CharField(max_length=20)
    endDate = models.CharField(max_length=20)
    title = models.CharField(max_length=25)
    description = models.CharField(max_length=200)
    long_description = models.TextField(null=True)
    totalPrice = models.IntegerField()
    img = models.ImageField(blank=True, upload_to='images/')


class Profile(AbstractUser):
    id = models.AutoField(primary_key=True)
    name = models.CharField(default='None', max_length=30)
    email = models.EmailField(default='admin@admin.com')
    username = models.CharField(unique=True, max_length=20)
    password = models.CharField(default='None', max_length=20)
    phone = models.CharField(default='None', max_length=16)
    address = models.TextField(default='None')


class Bookings_From_User(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(to=Profile, on_delete=models.SET_NULL, null=True)
    event_id = models.ForeignKey(to=Event, on_delete=models.SET_NULL, null=True)


class Donates_From_User(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(to=Profile, on_delete=models.SET_NULL, null=True)
    donate_id = models.ForeignKey(to=Donate, on_delete=models.SET_NULL, null=True)
