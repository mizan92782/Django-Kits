from django.urls import path
from . import views  # import views from the current app

urlpatterns = [
    path('response/', views.response_view, name='res'),
]
