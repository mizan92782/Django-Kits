from email import contentmanager
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin,BaseUserManager

# Create your models here.


class UserManager(BaseUserManager):
    

    #! create new User
    def creat_user(self,email,first_name,last_name,password,institute,contact_number,date_joined,*extra_fields):
        

        if not email or not password or not institute:
            raise ValueError("Email or password or institute cannot be empty")
        
        
        #notmalize email
        email = self.normalize_email(email)

        #model instance create 
        user = self.model(
          email= email,
          first_name=first_name,
          last_name= last_name,
          institute= institute,
          
          contact_number = contact_number,
          date_joined= date_joined


        )

        #password set,
        user.set_password(password)

        # save model 
        user.save(using=self._db)
        return user
    
    

    def create_superuser(self, email,first_name,last_name,password,institute,contact_number,date_joined,*extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        return self.create_user(email, first_name, last_name, password, **extra_fields)



   


class  User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)  # Email হবে login credential
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    institute = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    contact_number = models.CharField(max_length=15, blank=True, null=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    
    # Permissions related fields
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False) 
    is_superuser = models.BooleanField(default=False) 

    #credintial field
    USERNAME_FIELD= 'email'


    # Manager: Manage how use will create
    object= UserManager()
    

    USERNAME_FIELD = 'email'        # Email will be used instead of username
    REQUIRED_FIELDS = ['first_name', 'last_name']

    #custom method
    def get_ful_name(self):
       return f'{self.first_name} {self.last_name}'



    def is_staff(self):
      return self.is_staff
    
    def is_super(self):
      return self.is_superuser
    
    def is_super(self):
      return self.is_active
    
    
    def save(self,*args, **kwargs):
       self.first_name = self.first_name.title()
       return super.save(*args, **kwargs)
  
    
    
  

    
   
