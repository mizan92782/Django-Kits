from django.http import HttpResponse, HttpResponseBadRequest
from django.shortcuts import get_object_or_404, render

from tempt.models import Student
from django.db.models import Q

# Create your views here.

def routerStudent(self,id=None,name=None,age=None,batch=None):
  stu =None
  
  if id: 
    stu = get_object_or_404(Student,id=id)
    
  if id and age :
    stu = Student.objects.filter(Q(id__gt=id) & Q(age__gte=age)).all()
  if id and age  and name:
   stu = Student.objects.filter(Q(id__gt=id) & Q(age__gte=age) & Q(name__contains=name)).all()

  for x in stu:
    print(x.id ,x.name , x.age , x.batch )
  return HttpResponse("apple")

