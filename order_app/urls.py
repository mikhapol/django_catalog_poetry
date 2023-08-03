from django.urls import path

from order_app.apps import OrderAppConfig
from order_app.views import OrderCreateView

app_name = OrderAppConfig.name


urlpatterns = [

    path('create/<int:pk>', OrderCreateView.as_view(), name='order_create'),

]
