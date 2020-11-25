from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser


class Events(models.Model):
    id = models.AutoField(primary_key=True)
    startDate = models.TextField()
    endDate = models.TextField()
    title = models.TextField()
    description = models.TextField()
    img = models.ImageField(upload_to='upload/', default='static/hehe.jpg')
    address = models.TextField()


class Donate(models.Model):
    id = models.AutoField(primary_key=True)
    startDate = models.TextField()
    endDate = models.TextField()
    title = models.TextField()
    description = models.TextField()
    totalPrice = models.IntegerField()
    img = models.ImageField(upload_to='upload/', default='static/hehe.jpg')


class Profile(AbstractUser):
    id = models.AutoField(primary_key=True)
    name = models.TextField(default='None')
    email = models.EmailField(default='admin@admin.com')
    password = models.TextField(default='None')
    phone = models.TextField(default='None')
    address = models.TextField(default='None')


class Booking(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(to=Profile, on_delete=models.SET_NULL, null=True)
    event_id = models.ForeignKey(to=Events, on_delete=models.SET_NULL, null=True)


class Donates(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(to=Profile, on_delete=models.SET_NULL, null=True)
    donate_id = models.ForeignKey(to=Donate, on_delete=models.SET_NULL, null=True)
