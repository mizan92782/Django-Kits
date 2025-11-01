

from django.urls import path
from . import views

urlpatterns = [
    path('id/<int:id>/' ,  views.routerStudent,name='id'),
    path('id/age/<int:id>/<int:age>/' ,  views.routerStudent,name='id_age'),
    path('id/age/name/<int:id>/<int:age>/<str:name>/' ,  views.routerStudent,name='id_age_name')
]
