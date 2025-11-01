from django.contrib import admin

from enums.student_enum import Department
from .models import Student

# Register your models here.

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
  list_display=['name','roll','batch','department','birth','age','gender','medium']
  readonly_fields=['age']
    
