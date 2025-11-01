from django.db import connection
from django.shortcuts import render
from .models import Restaurant, Staff

from django.http import HttpResponse

def restaurant_view(request):
    return HttpResponse("<h4>This is apple how are you</h4>")