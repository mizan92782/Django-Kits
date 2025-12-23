from django.shortcuts import render
from rest_framework import generics
from myapp.models import User
from myapp.serializers import UserRegisterSerializer
from rest_framework.response import Response

from rest_framework import generics, status
from rest_framework.response import Response

class UserCreateView(generics.CreateAPIView):
    serializer_class = UserRegisterSerializer
    queryset = User.objects.all()

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)
        