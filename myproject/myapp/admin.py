from django.contrib import admin
from .models import Product, Orders, Dispatch, Customer


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price')
    list_display_links = ('id', 'name', 'price')


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'adress', 'phone')
    list_display_links = ('id', 'name', 'adress', 'phone')


@admin.register(Orders)
class OrdersAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer', 'contract_number', 'date_contract', 'name', 'shipment')
    list_display_links = ('id', 'customer', 'contract_number', 'date_contract', 'name', 'shipment')


@admin.register(Dispatch)
class DispatchAdmin(admin.ModelAdmin):
    list_display = ('id', 'id_orders', 'date_shipment', 'dispatch_count')
    list_display_links = ('id', 'id_orders', 'date_shipment', 'dispatch_count')