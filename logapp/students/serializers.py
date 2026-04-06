from rest_framework import serializers
from .models import Student, Teacher


class TeacherSerializer(serializers.ModelSerializer):
    """Serializer for Teacher model"""
    class Meta:
        model = Teacher
        fields = ['id', 'name', 'email', 'subject', 'experience_years', 'created_at', 'updated_at']
        read_only_fields = ['created_at', 'updated_at']


class StudentSerializer(serializers.ModelSerializer):
    """Serializer for Student model"""
    teacher_name = serializers.CharField(source='teacher.name', read_only=True)
    
    class Meta:
        model = Student
        fields = ['id', 'name', 'email', 'roll_number', 'grade', 'teacher', 'teacher_name', 'enrollment_date', 'created_at', 'updated_at']
        read_only_fields = ['enrollment_date', 'created_at', 'updated_at']
