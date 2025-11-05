from functools import partial
import django.core.asgi
import rest_framework
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from core.serializers import ProductSerializer
from core.models import Product
from rest_framework import status
from rest_framework.permissions import IsAuthenticated


from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from core.models import Product
from core.serializers import ProductSerializer
from .Permissions.permisison_check import IsPremiumUser   #customize permisoion clalss
#! permission class for check permisson







@api_view(['GET', 'POST'])
@permission_classes([IsPremiumUser])  #custom permission check
def product_show_create(request):
    # GET - সব প্রোডাক্ট দেখাবে
    if request.method == 'GET':
        print( "-------------",request.user.username)
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response({'data': serializer.data})
    
    # POST - নতুন প্রোডাক্ট তৈরি করবে
    elif request.method == 'POST':
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'data': serializer.data}, status=status.HTTP_201_CREATED)
        return Response({'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)









#! for update need pk,so need another funtion
#! in funtion view data update by json,so it not a easyway


@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def single_product_details(request, pk):
    try:
        product = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        return Response({'error': 'Product not found'}, status=status.HTTP_404_NOT_FOUND)

    # GET - একক প্রোডাক্ট দেখানো
    if request.method == 'GET':
        serializer = ProductSerializer(product)
        return Response({'data': serializer.data})

    # PUT - পুরো আপডেট
    elif request.method == 'PUT':
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'data': serializer.data})
        return Response({'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    # PATCH - আংশিক আপডেট
    elif request.method == 'PATCH':
        serializer = ProductSerializer(product, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'data': serializer.data})
        return Response({'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    # DELETE - ডিলিট করা
    elif request.method == 'DELETE':
        product.delete()
        return Response({'message': 'Product deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
