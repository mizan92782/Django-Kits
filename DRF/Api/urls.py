
import rest_framework

from Api import function_view,views
from django.urls import path


urlpatterns = [
    path('loguser/', views.auto_login, name='log'),
    path('products/', function_view.product_show_create, name='product-list'),
    path('products/<int:pk>/', function_view.single_product_details, name='product-detail'),
]