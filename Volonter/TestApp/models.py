from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User

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

class Comment(models.Model):
  post = models.ForeignKey(Post, on_delete = models.CASCADE, related_name ='comments')
  user = models.ForeignKey(User, on_delete = models.CASCADE)
  content = models.TextField()

class Post(models.ModelForm):
    image = models.ImageField()
    default="default_foo.png", upload_to="post_picture")
    caption = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.author.username}\'s Post- {self.title}'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.image.path)
        if img.height > 400 or img.width > 400:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)




        #ie = Events(date='12/12/12', title="Разз ва", description='dfgef', src='123.jpg')
#ie.save()

######OR THIS WAY COMMENTS
class Comment(model.Models):
    post = models.ForeignKey(Post, related_name=post)
    name = models.CharField()
    body = models.TextField()
    date_added = models.DateTimeField()

    def __str__ (self):
        return '%s - %s' % (self.post.name)
