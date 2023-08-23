from django.contrib import admin

from app_order.models import Order


# Register your models here.
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('product', 'email', 'created_at',)
    list_filter = ('product',)
