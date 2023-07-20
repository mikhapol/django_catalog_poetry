from django.contrib import admin

from catalog_app.models import Product, Category


# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'desc',)
    list_filter = ('name',)
    # search_fields = ('name', 'desc',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'price', 'category', 'created_at', 'update_at',)
    list_filter = ('name',)
    search_fields = ('name', 'desc',)
