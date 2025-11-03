from django.contrib import admin
from .models import Applicant, User

class ApplicantAdmin(admin.ModelAdmin):
    list_display = [
        field.name for field in Applicant._meta.get_fields()
        if field.concrete and not (field.many_to_many or field.one_to_many)
    ]

admin.site.register(Applicant, ApplicantAdmin)


class UserAdmin(admin.ModelAdmin):
    list_display = [
        field.name for field in User._meta.get_fields()
        if field.concrete and not (field.many_to_many or field.one_to_many)
    ]

admin.site.register(User, UserAdmin)
