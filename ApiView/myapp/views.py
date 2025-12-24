from django.shortcuts import render
from rest_framework import generics, viewsets
from myapp.models import Customer, Post, User, Book
from myapp.serializers import PostCreateSerializer, UserRegisterSerializer, BookSerializer
from rest_framework.response import Response

from rest_framework import generics, status
from rest_framework.response import Response

class UserCreateView(generics.CreateAPIView):
    serializer_class = UserRegisterSerializer
    queryset = Customer.objects.all()

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        
    
        
    # ============================================handle seralizer:
    '''
    
    def get_serializer_class(self):
    if self.request.user.is_staff:
        return AdminUserSerializer
    return UserRegisterSerializer
    

    
    '''
    
    
    
    
    #========================================= overide permissino
    '''
    def get_permissions(self):
    if self.request.method == "POST":
        return []
    return [IsAuthenticated()]
    
    
    '''
    



class UserListView(generics.ListAPIView):
  serializer_class = UserRegisterSerializer
  queryset = Customer.objects.all()
  ''' we sent instace and serilizer get every data of customer instace'''
  
  

  
  #====== user for override all() query. or filtering:also i can direct filter query in qaurysert
  def get_queryset(self):
    return Customer.objects.filter(age__lt=220)
    '''override ----> queryset'''
    
    
    
    
class PostCreateView(generics.ListCreateAPIView):
    serializer_class = PostCreateSerializer
    queryset = Post.objects.select_related('user')
    
    #! VVI : post create korer somoy,automatically user catch kore user field a set kore:
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        '''Client ──POST──> API ──>request.user──> perform_create ---> seriaizer ─> creaete()-->save(user=...)──> Model'''


class BookListCreateView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    
class BookRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    