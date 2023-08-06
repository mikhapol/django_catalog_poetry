__all__ = [
    'VegetablesListView',
    'ProviderCreateView',
    'ProviderUpdateView',
    'ProductListView',
    'ProductCreateView',
    'ProductUpdateView',
    'ProductDetailView',
    'ProductDeleteView',
    'ContactTemplateView',
    'CategoryListView',
]

from catalog_app.views.category import CategoryListView
from catalog_app.views.contact import ContactTemplateView
from catalog_app.views.product import ProductListView, ProductCreateView, ProductUpdateView, ProductDetailView, \
    ProductDeleteView
from catalog_app.views.provider import ProviderCreateView, ProviderUpdateView
from catalog_app.views.vegetables import VegetablesListView
