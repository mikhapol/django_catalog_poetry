from django.urls import path

from catalog_app.apps import CatalogAppConfig
from catalog_app.views import contacts, ProductListView, CategoryListView, ProductCreateView, ProductUpdateView, \
    ProductDetailView, ProductDeleteView, admin, VegetablesListView, vegetables

app_name = CatalogAppConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name='index'),
    path('categories/', CategoryListView.as_view(), name='categories'),

    path('catalog_app/view/<int:pk>/', ProductDetailView.as_view(), name='view_product'),
    path('catalog_app/create/', ProductCreateView.as_view(), name='create_product'),
    path('catalog_app/update/<int:pk>/', ProductUpdateView.as_view(), name='update_product'),
    path('catalog_app/delete/<int:pk>/', ProductDeleteView.as_view(), name='delete_product'),

    # path('/catalog_app/<int:pk>/vegetables/', VegetablesListView.as_view(), name='vegetables'),
    path('catalog_app/<int:pk>/vegetables/', vegetables, name='vegetables'),

    path('contacts/', contacts, name='contacts'),
    path('admin/', admin, name='admin'),
]
