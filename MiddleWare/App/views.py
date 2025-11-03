from urllib import response
from django.shortcuts import render

# Create your views here.
def home(request):
  print("view--------------")
  return render(response,'home.html')