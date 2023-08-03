from django.urls import path

from catalog_app.apps import CatalogAppConfig
from catalog_app.views import ProductListView, CategoryListView, ProductCreateView, ProductUpdateView, \
    ProductDetailView, ProductDeleteView, VegetablesListView, ContactTemplateView, ProviderCreateView, \
    ProviderUpdateView

app_name = CatalogAppConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name='index'),
    path('catalog_app/categories/', CategoryListView.as_view(), name='categories'),

    path('catalog_app/view/<int:pk>/', ProductDetailView.as_view(), name='view_product'),
    path('catalog_app/create_product/', ProductCreateView.as_view(), name='create_product'),
    path('catalog_app/update_product/<int:pk>/', ProductUpdateView.as_view(), name='update_product'),
    path('catalog_app/delete/<int:pk>/', ProductDeleteView.as_view(), name='delete_product'),

    path('catalog_app/<int:pk>/vegetables/', VegetablesListView.as_view(), name='vegetables'),
    # path('catalog_app/<int:pk>/vegetables/', vegetables, name='vegetables'),

    path('catalog_app/contacts/', ContactTemplateView.as_view(), name='contacts'),
    # path('contacts/', contacts, name='contacts'),

    path('<int:pk>/catalog_app/create_provider/', ProviderCreateView.as_view(), name='create_provider'),
    path('<int:pk>/catalog_app/update_provider/', ProviderUpdateView.as_view(), name='update_provider'),

]
