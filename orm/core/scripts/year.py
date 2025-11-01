from datetime import timedelta

import django
from django.db import connection
from core.models import Restaurant,Staff
from django.db.models import F

def run():

  boy = Staff.objects.values('name', 'restaurant__name')

  for x in boy:
      print(f"{x['name']} -- {x['restaurant__name']}")

  print('\n'*3)
  print(len(connection.queries))
  
  