from django.db import models



# Create your models here.


class Product(models.Model):
    title =  models.CharField()
    price = models.IntegerField()
    status = models.CharField(default="Normal")

class OrderItem(models.Model):
    product = models.ForeignKey(Product,related_name="orderitem",on_delete= models.CASCADE)
    quantity =models.IntegerField()
    total_pro_price = models.IntegerField(null=True,blank=True)
    def save(self, *args, **kwargs):
        self.total_pro_price=  self.quantity * self.product.price
    
        super().save(*args, **kwargs)