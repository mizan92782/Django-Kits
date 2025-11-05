from django.contrib.auth.models import Permission, Group, User
from django.contrib.contenttypes.models import ContentType
from core.models import Product


def run():

  #! create group
  BasicUser,_ = Group.objects.get_or_create(name="BasicUser")
  PremiumUser,_ = Group.objects.get_or_create(name="PremiumUser")


  # ! now we will give this  geting permissions
  # get content
  content_type = ContentType.objects.get(app_label='core', model='product')


  add_pro = Permission.objects.get(codename='add_product', content_type=content_type)
  change_pro = Permission.objects.get(codename='change_product', content_type=content_type)
  view_pro= Permission.objects.get(codename='view_product', content_type=content_type)
  delete_pro = Permission.objects.get(codename='delete_product', content_type=content_type)



# ! now add this permission to  groups

  BasicUser.permissions.add(view_pro,)
  PremiumUser.permissions.add(view_pro,change_pro)