import random
from product.models import Product


def run():
    for x in range(1, 15):
        obj=Product.objects.create(
            name=f"Product {x}",
            price=random.uniform(100, 1000),   # price as float
            offer=random.randint(1, 10)        # offer as int
        )
        
        obj.save()
        