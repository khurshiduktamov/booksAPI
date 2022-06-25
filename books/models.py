from pyexpat import model
from turtle import title
from django.db import models

# Create your models here.

class Book(models.Model):
    name = models.CharField(max_length=150)
    title = models.CharField(max_length=250)
    author = models.CharField(max_length=200)
    isbn = models.CharField(max_length=13, unique=True)

    def __str__(self) -> str:
        return self.name

