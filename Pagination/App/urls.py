
from . import views
from django.urls import path

urlpatterns = [
  path('list/',views.student_list,name='student')
]