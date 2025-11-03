from . import views
from django.urls import path


urlpatterns = [
    path('form/',views.student_create,name='form')
]
