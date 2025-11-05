
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType

from core.models import Product


def run():
  
  content_type = ContentType.objects.get_for_model(Product)
  permissions = Permission.objects.filter(content_type=content_type)

  for p in permissions:
      print(p.codename, "-", p.name)