from django.shortcuts import render, redirect
from rest_framework import generics
from django.http import Http404
from .forms import NewOrderForm, NewProductForm, NewCustomerForm, NewDispatchForm
from .models import Product, Customer, Orders, Dispatch
from .serializers import ProductSerializer, OrdersSerializer, CustomerSerializer, DispatchSerializer
from django.views.generic import ListView, DeleteView, DetailView, UpdateView
from django.urls import reverse_lazy


def index(request):
    orders = Orders.objects.order_by('id')
    return render(request, 'myapp/index.html', {'orders': orders})


def product_dispatch(request):
    dispatch = Dispatch.objects.order_by('id')
    return render(request, 'myapp/product_dispatch.html', {'dispatch': dispatch} )


def product(request):
    products = Product.objects.order_by('id')
    return render(request, 'myapp/product.html', {'products': products})


def customer(request):
    customers = Customer.objects.order_by('id')
    return render(request, 'myapp/customer.html', {'customers': customers})


def dispatch(request):
    dispatchs = Dispatch.objects.order_by('id')
    return render(request, 'myapp/dispatch.html', {'dispatchs': dispatchs})


def set_orders(request):
    if request.method == 'POST':
        form = NewOrderForm(request.POST)
        form.instance.owner = request.user
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            raise Http404
    else:
        form = NewOrderForm()
    return render(request, 'myapp/neworder.html', {'form': form})


def set_products(request):
    if request.method == 'POST':
        form = NewProductForm(request.POST)
        form.instance.owner = request.user
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            raise Http404
    else:
        form = NewProductForm()
    return render(request, 'myapp/newproduct.html', {'form': form})


def set_customer(request):
    if request.method == 'POST':
        form = NewCustomerForm(request.POST)
        form.instance.owner = request.user
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            raise Http404
    else:
        form = NewCustomerForm()
    return render(request, 'myapp/newcustomer.html', {'form': form})


def set_dispatch(request):
    if request.method == 'POST':
        form = NewDispatchForm(request.POST)
        form.instance.owner = request.user
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            raise Http404
    else:
        form = NewDispatchForm()
    return render(request, 'myapp/newdispatch.html', {'form': form})


class OrdersDeleteView(DeleteView):
    model = Orders
    template_name = 'myapp/order_delete.html'
    success_url = reverse_lazy('home')


class OrdersUpdateView(UpdateView):
    model = Orders
    template_name = 'myapp/order_edit.html'
    fields = '__all__'
    success_url = reverse_lazy('home')


class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'myapp/product_delete.html'
    success_url = reverse_lazy('home')


class ProductUpdateView(UpdateView):
    model = Product
    template_name = 'myapp/product_edit.html'
    fields = '__all__'
    success_url = reverse_lazy('home')


class CustomerDeleteView(DeleteView):
    model = Customer
    template_name = 'myapp/customer_delete.html'
    success_url = reverse_lazy('home')


class CustomerUpdateView(UpdateView):
    model = Customer
    template_name = 'myapp/customer_edit.html'
    fields = '__all__'
    success_url = reverse_lazy('home')


class DispatchDeleteView(DeleteView):
    model = Dispatch
    template_name = 'myapp/dispatch_delete.html'
    success_url = reverse_lazy('home')


class DispatchUpdateView(UpdateView):
    model = Dispatch
    template_name = 'myapp/dispatch_edit.html'
    fields = '__all__'
    success_url = reverse_lazy('home')
