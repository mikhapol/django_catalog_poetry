from django.views.generic import ListView
from catalog_app.models import Product, Category


class VegetablesListView(ListView):
    model = Product

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(category_id=self.kwargs.get('pk'))
        return queryset

    def get_context_data(self, *args, **kwargs):
        contex_data = super().get_context_data(*args, **kwargs)

        category_item = Category.objects.get(pk=self.kwargs.get('pk'))
        contex_data['category_id'] = category_item.pk,
        contex_data['title'] = f'Все продукты категории {category_item.name}'

        return contex_data
