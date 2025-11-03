
from django.contrib.auth.models import User,Group

def run():

  name= ['mizan','sizan','arif','karim']
  password="abc"

  


  users = User.objects.all()

  for x in users:
    print (x.username)

  