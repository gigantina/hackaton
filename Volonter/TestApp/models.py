from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser


class Profile(AbstractUser):
    id = models.AutoField(primary_key=True)
    name = models.CharField(default='', max_length=30)
    email = models.EmailField(default='')
    username = models.CharField(unique=True, max_length=20)
    password = models.CharField(default='', max_length=20)
    phone = models.CharField(default='', max_length=16)
    address = models.TextField(default='')


class CategoryHelp(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(default='', max_length=300)


class Event(models.Model):
    id = models.AutoField(primary_key=True)
    startDate = models.CharField(max_length=20)
    endDate = models.CharField(max_length=20)
    title = models.CharField(max_length=25)
    description = models.CharField(max_length=200)
    long_description = models.TextField(null=True)
    img = models.ImageField(blank=True, upload_to='images/')
    address = models.TextField()
    category_help = models.ForeignKey(to=CategoryHelp, on_delete=models.SET_NULL, null=True)
    owner = models.ForeignKey(to=Profile, on_delete=models.SET_NULL, default=1, null=True)


class Donate(models.Model):
    id = models.AutoField(primary_key=True)
    startDate = models.CharField(max_length=20)
    endDate = models.CharField(max_length=20)
    title = models.CharField(max_length=25)
    description = models.CharField(max_length=300)
    long_description = models.TextField(null=True)
    totalPrice = models.IntegerField()
    img = models.ImageField(blank=True, upload_to='images/')


class Achievment(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(default='', max_length=30)
    description = models.CharField(default='', max_length=300)


class Bookings_From_User(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(to=Profile, on_delete=models.SET_NULL, null=True)
    event_id = models.ForeignKey(to=Event, on_delete=models.SET_NULL, null=True)


class Donates_From_User(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(to=Profile, on_delete=models.SET_NULL, null=True)
    donate_id = models.ForeignKey(to=Donate, on_delete=models.SET_NULL, null=True)


class Achievments_From_User(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(to=Profile, on_delete=models.SET_NULL, null=True)
    achive_id = models.ForeignKey(to=Achievment, on_delete=models.SET_NULL, null=True)


class UuidAndEmail(models.Model):
    id = models.AutoField(primary_key=True)
    uuid = models.CharField(max_length=60)
    email = models.CharField(max_length=200)
    action = models.IntegerField()
