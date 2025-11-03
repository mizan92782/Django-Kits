from django.urls import path
from . import views


urlpatterns=[
  path('register/', views.apply_page, name='apply_page')
]