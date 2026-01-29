from product.models import Product
from django.db.models import Sum, Max

def run():
    # Annotate total_quantity
    products = Product.objects.annotate(
        total_quantity=Sum('orderitem__quantity')
    )

    # Find max quantity
    best_quantity = products.aggregate(max_qty=Max('total_quantity'))['max_qty'] or 0

    # Loop & save
    for product in products:
        quantity = product.total_quantity or 0
        if quantity == best_quantity and best_quantity > 0:
            product.status = 'Best Seller'
        elif quantity > 7:
            product.status = 'Trending'
        elif quantity > 5:
            product.status = 'Popular'
        else:
            product.status = 'Normal'
        product.save()

    # Print all
    for product in Product.objects.annotate(total_quantity=Sum('orderitem__quantity')):
        quantity = product.total_quantity or 0
        print(f"{product.title} | Price: {product.price} | Total Sold: {quantity} | Status: {product.status}")
