from django.contrib import admin
from .models import Student, Teacher

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'experience_years', 'created_at')
    search_fields = ('name', 'email', 'subject')
    list_filter = ('subject', 'created_at')

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'roll_number', 'email', 'grade', 'teacher', 'created_at')
    search_fields = ('name', 'roll_number', 'email')
    list_filter = ('grade', 'teacher', 'created_at')
    raw_id_fields = ('teacher',)
