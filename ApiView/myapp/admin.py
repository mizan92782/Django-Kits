from myapp.models import User, Book
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User, Customer, Address, Post, Book

class UserAdmin(BaseUserAdmin):
    model = User

    list_display = ("email", "is_staff", "is_active")
    list_filter = ("is_staff", "is_active")

    fieldsets = (
        (None, {"fields": ("email", "password")}),
        ("Permissions", {"fields": ("is_staff", "is_superuser", "is_active", "groups", "user_permissions")}),
    )

    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("email", "password1", "password2", "is_staff", "is_superuser"),
        }),
    )

    search_fields = ("email",)
    ordering = ("email",)
  
admin.site.register(User, UserAdmin)



@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ("city", "zip_code")
    search_fields = ("city", "zip_code")
  
@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ("name", "user", "phone", "age", "address")
    search_fields = ("name", "phone", "user__email")
    list_filter = ("age", "address")

    
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "user", "created_at")
    search_fields = ("title", "user__email")
    list_filter = ("created_at",)
    

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "published_date", "isbn")
    search_fields = ("title", "author", "isbn")
    list_filter = ("published_date",)
