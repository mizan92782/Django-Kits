from django.db.models import Q

from ..models import Sale

def run():
  
  q= Q(income__gt=120)
  n= ~Q(restaurant__name__contains='a')
  
  obj = Sale.objects.filter(q & n)
  
  for x in obj:
    print(x.restaurant.name , x.income)
  
  
  
  
  