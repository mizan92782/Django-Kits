from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from .models import Customer
from .serializers import CustomerSerializer


class CustomerAPIView(APIView):

    @swagger_auto_schema(
        operation_description="Retrieve all customers or a single customer",
        responses={200: CustomerSerializer(many=True)}
    )
    def get(self, request, pk=None):
        if pk:
            try:
                customer = Customer.objects.get(pk=pk)
            except Customer.DoesNotExist:
                return Response({"error": "Customer not found"}, status=404)
            serializer = CustomerSerializer(customer)
            return Response(serializer.data)

        customers = Customer.objects.all()
        serializer = CustomerSerializer(customers, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(
        operation_description="Create a new customer",
        request_body=CustomerSerializer,   # ⭐ MOST IMPORTANT
        responses={201: CustomerSerializer}
    )
    def post(self, request):
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    @swagger_auto_schema(
        operation_description="Update a customer",
        request_body=CustomerSerializer,   # ⭐ Needed for PUT
        responses={200: CustomerSerializer}
    )
    def put(self, request, pk=None):
        if not pk:
            return Response({"error": "ID required for update"}, status=400)

        try:
            customer = Customer.objects.get(pk=pk)
        except Customer.DoesNotExist:
            return Response({"error": "Customer not found"}, status=404)

        serializer = CustomerSerializer(customer, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    @swagger_auto_schema(
        operation_description="Delete a customer",
        responses={204: "Customer deleted"}
    )
    def delete(self, request, pk=None):
        if not pk:
            return Response({"error": "ID required for delete"}, status=400)

        try:
            customer = Customer.objects.get(pk=pk)
        except Customer.DoesNotExist:
            return Response({"error": "Customer not found"}, status=404)

        customer.delete()
        return Response({"message": "Deleted successfully"}, status=204)
        