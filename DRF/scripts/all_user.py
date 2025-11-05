
from core.models import User
def run():


  users = User.objects.all()
  for x  in users:
  
        print(x.username)