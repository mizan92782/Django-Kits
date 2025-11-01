
from django.db import connection
from ..models import Restaurant


def run():
  res_name = [Restaurant.TypeChoices.CHINESE,
              Restaurant.TypeChoices.ITALIAN,
              Restaurant.TypeChoices.MEXICAN]
  
  
  # find all these Restaurant
  
  restaurant = Restaurant.objects.filter(restaurant_type__in=res_name)
  
  
  print(restaurant.count())
  
  
  print('\n'*3)
  print(connection.queries)
  
  
  
  