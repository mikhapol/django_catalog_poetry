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

from app_catalog.views.category import CategoryListView
from app_catalog.views.contact import ContactTemplateView
from app_catalog.views.product import ProductListView, ProductCreateView, ProductUpdateView, ProductDetailView, \
    ProductDeleteView
from app_catalog.views.provider import ProviderCreateView, ProviderUpdateView
from app_catalog.views.vegetables import VegetablesListView
