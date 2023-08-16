from django.contrib import admin

from catalog_app.models import Product, Category, Owner, Version


# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'desc',)
    list_filter = ('name',)
    # search_fields = ('name', 'desc',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'price', 'category', 'owner', 'created_at', 'update_at',)
    list_filter = ('name',)
    search_fields = ('name', 'desc',)


@admin.register(Owner)
class OwnerAdmin(admin.ModelAdmin):
    list_display = ('name', 'email',)
    list_filter = ('name',)
    search_fields = ('name', 'email',)


@admin.register(Version)
class VersionAdmin(admin.ModelAdmin):
    list_display = ('product', 'version_name', 'version_number', 'is_actual')
