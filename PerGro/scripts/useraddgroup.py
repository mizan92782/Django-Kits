
from django.contrib.auth.models import User,Group



def run():
  mizan = User.objects.filter(username='mizan')
  sizan = User.objects.filter(username='sizan')
  arif = User.objects.filter(username='arif')

  
  # arif is register
  Register = Group.objects.get(name='Register')
  
  #sizan is teacher
  Teacher = Group.objects.get(name='Teacher')



  # now add in Group
  arif.groups.add(Register)
  sizan.groups.add(Teacher)