from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response

from students.models import Father, Student
from students.serializer import FatherSerializer
# Create your views here.

class StudentView(ModelViewSet):
    
    def get_serializer_class(self):
        return FatherSerializer
    
    def get_queryset(self):
        return Father.objects.all()
        
    
    def list(self,request):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
        
