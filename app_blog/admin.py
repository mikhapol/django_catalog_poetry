from django.contrib import admin

from app_blog.models import Blog


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('name_blog', 'body', 'created_at', 'published', 'views_count',)
    list_filter = ('created_at',)
    search_fields = ('name_blog',)

