from django import forms
from .models import Orders, Product,Customer,Dispatch
from datetime import date, datetime


class NewOrderForm(forms.ModelForm):
    date_contract = forms.DateTimeField(label='Дата создания договора', input_formats='%Y-%m-%d %H:%M:%S', initial=datetime.now(),
                                        widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}))

    class Meta:
        model = Orders
        fields = ['customer', 'contract_number', 'date_contract', 'name', 'shipment']

class NewProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ['name', 'price']

class NewCustomerForm(forms.ModelForm):

    class Meta:
        model = Customer
        fields = ['name', 'adress','phone']

class NewDispatchForm(forms.ModelForm):

    class Meta:
        model = Dispatch
        fields = ['id_orders', 'date_shipment','dispatch_count']
