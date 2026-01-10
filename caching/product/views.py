import time
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework.generics import ListCreateAPIView

from product.models import Product
from product.serializer import ProductSerializer


PRODUCT_LIST_CACHE_PREFIX = "product_list_view"


@method_decorator(
    cache_page(60 * 15, key_prefix=PRODUCT_LIST_CACHE_PREFIX),
    name="list"
)
class ProductView(ListCreateAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()

    def get_queryset(self):
        print("🟥 CACHE MISS → DB HIT")
        time.sleep(5)
        return super().get_queryset()

    def list(self, request, *args, **kwargs):
        print("🟦 LIST VIEW EXECUTED")
        return super().list(request, *args, **kwargs)
        