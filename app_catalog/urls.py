from django.urls import path
from django.views.decorators.cache import cache_page

from app_catalog.apps import AppCatalogConfig
from app_catalog.views import ProductListView, CategoryListView, ProductCreateView, ProductUpdateView, \
    ProductDetailView, ProductDeleteView, VegetablesListView, ContactTemplateView, ProviderCreateView, \
    ProviderUpdateView

app_name = AppCatalogConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name='index'),
    path('app_catalog/categories/', cache_page(60)(CategoryListView.as_view()), name='categories'),

    path('app_catalog/view/<int:pk>/', cache_page(60)(ProductDetailView.as_view()), name='view_product'),
    path('app_catalog/create_product/', ProductCreateView.as_view(), name='create_product'),
    path('app_catalog/update_product/<int:pk>/', ProductUpdateView.as_view(), name='update_product'),
    path('app_catalog/delete/<int:pk>/', ProductDeleteView.as_view(), name='delete_product'),

    path('app_catalog/<int:pk>/vegetables/', VegetablesListView.as_view(), name='vegetables'),
    # path('app_catalog/<int:pk>/vegetables/', vegetables, name='vegetables'),

    path('app_catalog/contacts/', cache_page(60)(ContactTemplateView.as_view()), name='contacts'),
    # path('contacts/', contacts, name='contacts'),

    path('<int:pk>/app_catalog/create_provider/', ProviderCreateView.as_view(), name='create_provider'),
    path('<int:pk>/app_catalog/update_provider/', ProviderUpdateView.as_view(), name='update_provider'),

]
