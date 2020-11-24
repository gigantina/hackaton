from django.db import models

class Events(models.Model):
    id = models.AutoField(primary_key=True)
    startDate = models.TextField()
    endDate = models.TextField()
    title = models.TextField()
    description = models.TextField()
    src = models.TextField()

class Donate(models.Model):
    id = models.AutoField(primary_key=True)
    startDate = models.TextField()
    endDate = models.TextField()
    title = models.TextField()
    description = models.TextField()
    totalPrice = models.IntegerField()
    src = models.TextField()

class Users(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField()
    phone = models.TextField()
    address = models.TextField()
    email = models.EmailField()
    password = models.TextField()


#ie = Events(date='12/12/12', title="Разз ва", description='dfgef', src='123.jpg')
#ie.save()
