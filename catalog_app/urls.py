from django.urls import path

from catalog_app.apps import CatalogAppConfig
from catalog_app.views import home, contacts, product

app_name = CatalogAppConfig.name

urlpatterns = [
    path('', home, name='home'),
    path('product/', product, name='product'),
    path('contacts/', contacts, name='contacts'),
]