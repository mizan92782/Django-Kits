
from django.contrib import admin
from django.urls import path, re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.urls import include


from customer.views import CustomerAPIView

schema_view = get_schema_view(
    openapi.Info(
        title="Customer API Documentation",
        default_version='v1',
        description="API documentation for Customer CRUD",
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('admin/', admin.site.urls),

    # Your app URLs
    
    path('customer/', CustomerAPIView.as_view(), name="customer-list-create"),
    path('customer/<int:pk>/', CustomerAPIView.as_view(), name="customer-detail"),
    
    # Swagger URLs
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]







