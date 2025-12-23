from django.contrib import admin
from customer.models import Customer
from order.models import Order


class OrderInline(admin.TabularInline):
    model = Order
    extra = 1


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'address', 'age')
    search_fields = ('first_name', 'last_name', 'address')
    inlines = [OrderInline]
    