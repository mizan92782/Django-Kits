
from django.core.exceptions import ValidationError
from django.db import models

class Father(models.Model):
    name = models.CharField(max_length=20)
    age = models.PositiveSmallIntegerField(default=0)
    salary = models.IntegerField(default=0) 

    
    def clean(self):
        if self.age < 30:
            raise ValidationError({'age': "Father age cannot be less than 30"})

    def save(self, *args, **kwargs):
        #its professinal to check model level validation every update or save
        self.full_clean() 
        self.name = self.name.title()
        super().save(*args, **kwargs) 

    def __str__(self):
        return self.name
        
        

        
class Mother(models.Model):
    name = models.CharField(max_length=20)
    age  = models.PositiveIntegerField(default=0)
    cash = models.IntegerField(default=10)
    
    
    def clean(self):
        if self.age < 25:
            raise ValidationError({'age': "Mother age cannot be less than 30"})

    def save(self, *args, **kwargs):
        self.name = self.name.title()
        super().save(*args, **kwargs) 

    def __str__(self):
        return self.name
        
        

        
class Parents(models.Model):
    father = models.ForeignKey(Father,on_delete=models.CASCADE)
    mother = models.ForeignKey(Mother,on_delete=models.CASCADE)
    
    

    
class Student(models.Model):
    name = models.CharField(max_length=30,default="student_name")
    department = models.CharField(max_length=20)
    age = models.IntegerField(default=0)
    salary =  models.PositiveBigIntegerField(default=0)
    parent = models.ForeignKey(Parents,on_delete=models.CASCADE)
    
    def save(self,*args, **kwargs):
        self.name = self.name.title()
        return super().save(kwargs)
    