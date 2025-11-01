from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    roll = models.IntegerField(unique=True)
    email = models.EmailField(unique=True)
    department = models.CharField(max_length=50)
    

    def __str__(self):
        return f"{self.name} ({self.roll})"
