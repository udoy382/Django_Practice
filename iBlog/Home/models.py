from django.db import models

# Create your models here.

class Contact(models.Model):
    username = models.CharField(max_length=30)
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=18)
    password1 = models.CharField(max_length=100)
    password2 = models.CharField(max_length=100)
    textarea = models.TextField()

    def __str__(self):
        return self.username


class allBlog(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=30)
    slug = models.CharField(max_length=100, default='')
    content = models.TextField()
    dateTime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title