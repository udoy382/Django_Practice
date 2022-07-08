from django.db import models

# Create your models here.


class Contact(models.Model):
    username = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    email = models.EmailField()
    password1 = models.CharField(max_length=200)
    password2 = models.CharField(max_length=200)
    textarea = models.TextField()

    def __str__(self):
        return self.username