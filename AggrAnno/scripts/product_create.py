
import random

from product.models import OrderItem, Product

def run():


    productlist =[]
    for x in range(20):
        productlist.append(
            Product(
                title=f"Product {x}",
                price = random.randint(100,200)
            )
        )

    Product.objects.bulk_create(productlist)


    order_item_list=[]

    for x in range(30):
        product_id = random.randint(1,20)

        product = Product.objects.get(id = product_id)

        order_item_list.append(
            OrderItem(
                product = product,
                quantity = random.randint(1,5)
            )
        )
    


    OrderItem.objects.bulk_create(order_item_list)



    print("successfully created")




        