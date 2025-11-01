from datetime import date
from django.db import models
from django.core.exceptions import ValidationError
from enums import student_enum

def batch_validator(batch):
    if batch not in range(10, 30):
        raise ValidationError("Batch must be in range 10-30")
      
def validate_birth(value):
    if value > date.today():
        raise ValidationError("Birth date cannot be in the future")
 
 
      
def calculate_age(birth_date):
  today = date.today()
  age = today.year - birth_date.year
  if (today.month, today.day) < (birth_date.month, birth_date.day):
    age -= 1
  return age
 
 
 
 
 
      
class Student(models.Model):
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    name = models.CharField(max_length=101, editable=False)
    roll = models.PositiveIntegerField(unique=True,editable=False )
    birth = models.DateField(validators=[validate_birth])
    age = models.PositiveIntegerField(editable=False)
    batch = models.PositiveSmallIntegerField(validators=[batch_validator])
    department = models.CharField(max_length=50, choices=student_enum.Department.choices)
    gender = models.CharField(max_length=10, choices=student_enum.Gender.choices)
    medium = models.CharField(max_length=20, choices=student_enum.Medium.choices)



     
     
    def save(self, *args, **kwargs):
       
        self.name = f"{self.fname.title()} {self.lname.title()}"
        
       
        self.age = calculate_age(self.birth)
        if not self.roll:
          last_roll = Student.objects.order_by('-roll').first()
          self.roll = (last_roll.roll + 1) if last_roll else 1
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
