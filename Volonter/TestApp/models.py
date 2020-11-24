from django.db import models

class Events(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.TextField()
    title = models.TextField()
    description = models.TextField()
    src = models.TextField()

#ie = Events(date='12/12/12', title="Разз ва", description='dfgef', src='123.jpg')
#ie.save()