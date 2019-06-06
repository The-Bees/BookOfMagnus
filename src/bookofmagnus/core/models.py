from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.TextField(unique=True)
    follows = models.ManyToManyField(to='Book')
