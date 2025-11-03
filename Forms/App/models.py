# myapp/models.py
from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    age = models.IntegerField()
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.name
