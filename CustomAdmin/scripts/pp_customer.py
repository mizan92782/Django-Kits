
from customer.models import Customer


def run():
    customers = [
        {"first_name": "John", "last_name": "Doe", "address": "123 Main St"},
        {"first_name": "Jane", "last_name": "Smith", "address": "456 Oak Ave"},
        {"first_name": "Alice", "last_name": "Johnson", "address": "789 Pine Rd"},
        {"first_name": "Bob", "last_name": "Brown", "address": "321 Maple St"},
        {"first_name": "Charlie", "last_name": "Davis", "address": "654 Elm St"},
        {"first_name": "Eva", "last_name": "Wilson", "address": "987 Cedar Ave"},
        {"first_name": "Frank", "last_name": "Miller", "address": "135 Birch Rd"},
        {"first_name": "Grace", "last_name": "Taylor", "address": "246 Spruce St"},
        {"first_name": "Hannah", "last_name": "Anderson", "address": "369 Walnut Ave"},
        {"first_name": "Ian", "last_name": "Thomas", "address": "159 Chestnut Rd"},
    ]

    for c in customers:
        Customer.objects.create(**c)

    print("10 customers added successfully!")
    