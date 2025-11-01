
from django.db import connection
from ..models import Restaurant,Rating,Sale


def run():
  
  print(Restaurant.objects.filter(id__gt=5).count())
  
  
  
  
  print('\n'*2)
  print(connection.queries)