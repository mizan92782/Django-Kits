from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.core.cache import cache

from product.models import Product
from product.views import PRODUCT_LIST_CACHE_PREFIX


@receiver(post_save, sender=Product)
@receiver(post_delete, sender=Product)
def clear_product_list_cache(sender, **kwargs):
    cache.delete_pattern(f"*{PRODUCT_LIST_CACHE_PREFIX}*")
    print("🟨 PRODUCT LIST VIEW CACHE CLEARED")
    