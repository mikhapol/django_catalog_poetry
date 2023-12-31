from django.urls import path
from django.views.decorators.cache import cache_page

from app_blog.apps import AppBlogConfig
from app_blog.views import BlogListView, BlogCreateView, BlogDetailView, BlogUpdateView, BlogDeleteView, toggle_activity

app_name = AppBlogConfig.name

urlpatterns = [
    path('', BlogListView.as_view(), name='list'),
    path('create/', BlogCreateView.as_view(), name='create'),
    path('view/<int:pk>', BlogDetailView.as_view(), name='view'),
    path('edit/<int:pk>', BlogUpdateView.as_view(), name='edit'),
    path('delete/<int:pk>', BlogDeleteView.as_view(), name='delete'),
    path('activity/<int:pk>/', toggle_activity, name='activity'),
]