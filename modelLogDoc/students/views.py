from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import status
from yaml import serialize
from rest_framework.exceptions import ValidationError
from students.models import Father, Mother, Student
from students.serializer import FatherSerializer, MotherSerializer
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

class FahterView(ModelViewSet):
    
    #!get serialiser class
    def get_serializer_class(self):
        
        return FatherSerializer
    
        
        
        
    #! get initial queryset    
    def get_queryset(self):
        if self.action=='richfather':
            return Father.objects.filter(salary__gt=20000)
        
        return Father.objects.all()
    
    
    
    
    
    #! Filter that quer set,
    #! convert to number,because,query taka all as string
    #! or can usr BackendFilter for professionals
    def filter_queryset(self, queryset):
        age = self.request.query_params.get("age")
        salary = self.request.query_params.get("salary")
        
        if age is not None:
            try:
                age = int(age)
                queryset = queryset.filter(age__gt=age)
            except ValueError:
                raise ValidationError("Age must be an integer")
        
                
        if salary is not None:
            try:
                salary = int(salary)
                queryset = queryset.filter(salary__gt=salary)
            except ValueError:
                raise ValidationError("Salary must be an integer")
        
        return super().filter_queryset(queryset)
    
    
    
    
    #!documented API and Testiing UI  
    @swagger_auto_schema(
    operation_description="This API is used to crate or get all fateher list",
    manual_parameters=[
            openapi.Parameter('age', openapi.IN_QUERY, description=" Age", type=openapi.TYPE_INTEGER),
            openapi.Parameter('salary', openapi.IN_QUERY, description="Salary", type=openapi.TYPE_INTEGER),
            
        ]
    )  
    # List all Fathers
    def list(self, request):
        #! This line is very important to filter query
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
    
        
        
        
    # Create a Father with extra info in response
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        instance = serializer.save()
        
        #! add extra data in Object Create Response body
        return Response({
            "message": "A new Father instance created",
            "father_id": instance.id,
            "data": serialize.data
        }, status=status.HTTP_201_CREATED)
    
    
    @swagger_auto_schema(
        operation_description="This API is used to check rich fathers",
        manual_parameters=[
            openapi.Parameter('age', openapi.IN_QUERY, description=" Age", type=openapi.TYPE_INTEGER),
            openapi.Parameter('salary', openapi.IN_QUERY, description="Salary", type=openapi.TYPE_INTEGER),
            
        ]) 
    @action(detail=False)
    def richfather(self,request):
       #! This line is very important to filter query
        queryset = self.filter_queryset(self.get_queryset())
        serialize = self.get_serializer(queryset,many=True)
        return Response(serialize.data)

        
        
class MotherView(ModelViewSet):
    def get_serializer_class(self):
        
        return FatherSerializer
    
    def get_queryset(self):
        
        return Mother.objects.all()

    # List all Fathers
    def list(self, request):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
    
    # Create a Father with extra info in response
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        instance = serializer.save()
        
        return Response({
            "message": "A new Motherinstance created",
           
            "data":serializer.data
        }, status=status.HTTP_201_CREATED)
    
        