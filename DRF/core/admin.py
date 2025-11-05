from django.contrib import admin
from .models import User

@admin.register(User)
class Admin(admin.ModelAdmin):
  '''Admin View for '''

  list_display = ('username',)
  