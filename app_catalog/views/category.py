from django.views.generic import ListView
from app_catalog.models import Category


class CategoryListView(ListView):
    model = Category
    extra_context = {
        'title': 'Категория продуктов'
    }
