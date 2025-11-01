
from django.urls import path
from . import views

urlpatterns = [
    path('user/',views.UserCount,name='user_count'),
    path('create/',views.UserCreate,name='user-create'),
    path('home/',views.HomePage,name='homepage'),
    path('login/',views.LoginPage,name='login'),
]
