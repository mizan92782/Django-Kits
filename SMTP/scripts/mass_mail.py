
from django.core.mail import send_mass_mail

from django.conf import settings


def run():

  
  messages = (
      ('Hello User1', 'Your account created.', settings.EMAIL_HOST_USER, ['mizanmd92782@gmail.com']),
      ('Hello User2', 'Your password reset.', settings.EMAIL_HOST_USER, ['mizanmd92782@gmail.com']),
  )

  send_mass_mail(messages, fail_silently=False)