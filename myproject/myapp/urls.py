from django.urls import path
from . import views
from .views import set_orders, product, customer, dispatch, ProductUpdateView, ProductDeleteView, set_products, \
    set_customer, set_dispatch, CustomerUpdateView, CustomerDeleteView, DispatchUpdateView, DispatchDeleteView, \
    product_dispatch
from .views import (
    OrdersUpdateView,
    OrdersDeleteView,
)

urlpatterns = [
    path('', views.index, name='home'),
    path('neworder/', set_orders, name='neworder'),
    path('newproduct/', set_products, name='newproduct'),
    path('newcustomer/', set_customer, name='newcustomer'),
    path('newdispatch/', set_dispatch, name='newdispatch'),
    path('product/', product, name='product'),
    path('customer/', customer, name='customer'),
    path('dispatch/', dispatch, name='dispatch'),
    path('product-dispatch/', product_dispatch, name='product_dispatch'),
    path('order/<int:pk>/update', OrdersUpdateView.as_view(), name='order_edit'),
    path('order/<int:pk>/delete', OrdersDeleteView.as_view(), name='order_delete'),
    path('product/<int:pk>/update', ProductUpdateView.as_view(), name='product_edit'),
    path('product/<int:pk>/delete', ProductDeleteView.as_view(), name='product_delete'),
    path('customer/<int:pk>/update', CustomerUpdateView.as_view(), name='customer_edit'),
    path('customer/<int:pk>/delete', CustomerDeleteView.as_view(), name='customer_delete'),
    path('dispatch/<int:pk>/update', DispatchUpdateView.as_view(), name='dispatch_edit'),
    path('dispatch/<int:pk>/delete', DispatchDeleteView.as_view(), name='dispatch_delete'),

]
