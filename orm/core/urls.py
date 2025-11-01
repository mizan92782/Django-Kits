from django.urls import path
from . import views

urlpatterns = [
    path('', views.restaurant_view, name='restuarant'),  # ✅ corre
]
