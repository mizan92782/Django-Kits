


from .models import OrderItem, Product,Order,User
from rest_framework import serializers





class ProductSerializer(serializers.ModelSerializer):
  class Meta:
    model= Product 
    fields = '__all__'

    
    # field level validation: validate_fieldname
    def validate_price(self,value):
      if self.value <20 :
        raise serializers.ValidationError(
          "price must more thant 20"
        )
      return value



class OrderSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()  # শুধু username দেখাবে
    products= ProductSerializer(many=True,read_only= True)
    class Meta:
        model = Order
        fields = '__all__'




class OrderItemSerializer(serializers.ModelSerializer):
  product= ProductSerializer(read_only= True)
  order= OrderSerializer(read_only= True)
  class Meta:
    model= OrderItem
    fields = '__all__'








class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model= User
    fields = '__all__'







#! ======================= Api using Serializer Class : for custom data api =============

class Product_Inof_Serializer(serializers.Serializer):
      products = ProductSerializer(many=True) # for  all product_details
      count = serializers.IntegerField()
      max_price = serializers.IntegerField()
