

import django.db.models
from ..models import Product
from django.db.models import F, FloatField, ExpressionWrapper

def run():
  ls = Product.objects.annotate(
        loss=ExpressionWrapper(F('buy') - F('sell'), output_field=FloatField())
    ).filter(buy__gt=F('sell'))
  
  
  for x in ls :
    print(x.id ,x.buy, x.sell, x.loss)