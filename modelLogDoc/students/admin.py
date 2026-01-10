from django.contrib import admin

from students.models import Father, Mother, Parents
from django.contrib import admin

# Register your models here.
@admin.register(Father)
class FatherAdmin(admin.ModelAdmin):
    list_display = ("name",'age','salary')
    
@admin.register(Mother)
class MotherAdmin(admin.ModelAdmin):
    list_display = ("name",'age')
    
    
@admin.register(Parents)
class SpousAdmin(admin.ModelAdmin):
    list_display = ("father",'mother')
    
    
    
    