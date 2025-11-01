
from django.db.models import F, FloatField, ExpressionWrapper
from ..models import Sale


def run():
  
  Sale.objects.update(income=F('income')*2)
  