from django.urls import path

from app_order.apps import AppOrderConfig
from app_order.views import OrderCreateView

app_name = AppOrderConfig.name


urlpatterns = [

    path('create/<int:pk>', OrderCreateView.as_view(), name='order_create'),

]
