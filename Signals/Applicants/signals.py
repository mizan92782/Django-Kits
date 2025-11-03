
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from .models import Applicant, User


@receiver(post_save, sender=Applicant)
def create_user_for_application(sender,instance,created, **kwargs):

  if created:

    # signal: create user
    user= User.objects.create_user(
      email= instance.email,
      number= instance.number
    )



    #signal: send main
    send_mail(
            subject="Welcome to Our Platform",
            message=f"Hi {instance.first_name}, your account has been created. Login with your email: {user.email}",
            from_email="admin@django.com",
            recipient_list=[instance.email],
            fail_silently=False,
        )