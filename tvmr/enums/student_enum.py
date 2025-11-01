
from django.db import models



class Gender(models.TextChoices):
    MALE = "M", "Male"
    FEMALE = "F", "Female"
    OTHER = "O", "Other"






class Department(models.TextChoices):
    BSC = "BSc", "Bachelor of Science"
    BA = "BA", "Bachelor of Arts"
    BBA = "BBA", "Bachelor of Business Administration"
    BCOM = "BCom", "Bachelor of Commerce"
    MSC = "MSc", "Master of Science"
    MA = "MA", "Master of Arts"
    MBA = "MBA", "Master of Business Administration"
    PHD = "PhD", "Doctor of Philosophy"
    




class Medium(models.TextChoices):
  BANGLE = 'Bn','Bangla'
  ENGLISH ='Eng' ,'English'


