from django.urls import path
from django.views.decorators.cache import cache_page

from blog_app.apps import BlogAppConfig
from blog_app.views import BlogListView, BlogCreateView, BlogDetailView, BlogUpdateView, BlogDeleteView, toggle_activity

app_name = BlogAppConfig.name

urlpatterns = [
    path('', cache_page(60)(BlogListView.as_view()), name='list'),
    path('create/', BlogCreateView.as_view(), name='create'),
    path('view/<int:pk>', cache_page(60)(BlogDetailView.as_view()), name='view'),
    path('edit/<int:pk>', BlogUpdateView.as_view(), name='edit'),
    path('delete/<int:pk>', BlogDeleteView.as_view(), name='delete'),
    path('activity/<int:pk>/', toggle_activity, name='activity'),
]