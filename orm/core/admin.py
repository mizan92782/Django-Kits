from django.contrib import admin
from core.models import Restaurant, Sale, Rating, Student,Product

# Register your models here.
admin.site.register(Restaurant)
admin.site.register(Sale)
admin.site.register(Rating)
admin.site.register(Student)
admin.site.register(Product)