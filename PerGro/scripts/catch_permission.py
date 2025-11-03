
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from Permission.models import Student




def run():
  content_type = ContentType.objects.get(app_label='Permission',model='student')
  # catch any Permission
  per= Permission.objects.get(codename='add_student',content_type=content_type)

  print("catched permission : " ,per.codename)



  ''' now we can add this permissin in agoup 
  and add use in that group,so then people oly can crate student'''