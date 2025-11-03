from django.contrib.auth.models import Permission, Group, User
from django.contrib.contenttypes.models import ContentType
from Permission.models import Student


def run():

  #! create group
  Register,_ = Group.objects.get_or_create(name="Register")
  Teacher,_ = Group.objects.get_or_create(name="Teacher")


  # ! now we will give this  get permissions
  # get content
  content_type = ContentType.objects.get(app_label='Permission', model='student')


  add_per = Permission.objects.get(codename='add_student', content_type=content_type)
  filter_per = Permission.objects.get(codename='filter_student', content_type=content_type)
  change_per = Permission.objects.get(codename='change_student', content_type=content_type)
  search_per = Permission.objects.get(codename='search_student', content_type=content_type)
  view_per = Permission.objects.get(codename='view_student', content_type=content_type)



# ! now add this permission to  groups

  Register.permissions.add(add_per, view_per, change_per)
  Teacher.permissions.add(view_per,filter_per)