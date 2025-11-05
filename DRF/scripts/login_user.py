
from django.test import Client
from core.models import User

def run():
    client = Client()  # create a test client

    # Log in
    username = 'fuser3'
    user=User.objects.get(username=username) 
      # the password you set when creating the user
    client.force_login(user)
    print("✅ User is logged in (simulated):", user.username)
     


     #  client.logout()