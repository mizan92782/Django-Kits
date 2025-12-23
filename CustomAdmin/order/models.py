from django.db import models
from customer.models import Customer
from item.models import Item

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    on_create = models.DateField(auto_now_add=True)  # automatically set on creation

    def __str__(self):
        return f"Order {self.id} by {self.customer}"
        