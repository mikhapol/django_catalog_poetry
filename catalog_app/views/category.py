from django.views.generic import ListView
from catalog_app.models import Category


class CategoryListView(ListView):
    model = Category
    extra_context = {
        'title': 'Категория продуктов'
    }
