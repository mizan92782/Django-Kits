from django.shortcuts import render

from .models import Student
from django.core.paginator import Paginator

# Create your views here.

def student_list(request):
  
  std= Student.objects.all()

 

  # obeject per page
  paginator = Paginator(std,5)

  # page number
  page_number = request.GET.get('page')

  #page object
  page_obj= paginator.get_page(page_number)

  return render(request,'student.html',{'page_obj':page_obj})