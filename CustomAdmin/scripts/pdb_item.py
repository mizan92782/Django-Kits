from item.models import Item


def run():
    # Order of items to create
    items_to_create = [
        {"title": "Book", "price": 50},
        {"title": "Pen", "price": 30},
        {"title": "Table", "price": 33},
        {"title": "Shirts", "price": 22},
        {"title": "Orange", "price": 80},
        {"title": "Mango", "price": 50},
        {"title": "Krola", "price": 990},
        {"title": "Date", "price": 34},
    ]

    for item_data in items_to_create:
        Item.objects.create(**item_data)
        print(f"Created {item_data['title']} with price {item_data['price']}")