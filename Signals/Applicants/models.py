from random import choice
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
import Applicants
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.
def cv_path(instance,filename):
  return f'cv/{instance.first_name}_{instance.last_name}_{filename}'



class UserManager(BaseUserManager):
    def create_user(self, email, number, password=None, **extra_fields):
        
        user = User.objects.filter(email=email).first()
        if user :
            return  user
        


        if not email:
            raise ValueError("Email cannot be empty")
        if not number:
            raise ValueError("Number cannot be empty")

        email = self.normalize_email(email)
        user = self.model(email=email, number=number, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, number, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self.create_user(email, number, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    number = PhoneNumberField(unique=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["number"]

    def __str__(self):
        return self.email








# Applicant models
class Applicant(models.Model):
    class Position(models.TextChoices):
        JSWE = 'junior_SWE', "Junior SWE"
        SSWE = 'senior_SWE', "Senior SWE"
        ISWE = 'intern_SWE', "Intern SWE"

    email = models.EmailField(unique=True)
    number = PhoneNumberField(unique=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    age = models.PositiveSmallIntegerField()
    bio = models.TextField()
    position = models.CharField(max_length=20, choices=Position.choices)
    cv = models.FileField(upload_to=cv_path, blank=True, null=True)

    def __str__(self):
        return f"{self.first_name}'s application"
