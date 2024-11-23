from django.db import models


class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(verbose_name='Наименование товара', max_length=120)
    price = models.IntegerField(verbose_name='Цена')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['id']
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'


class Customer(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(verbose_name='Наименование заказчика', max_length=120)
    adress = models.CharField(verbose_name='Адрес заказчика', max_length=120)
    phone = models.CharField(verbose_name='Номер телефона', max_length=12)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['id']
        verbose_name = 'Заказчик'
        verbose_name_plural = 'Заказчики'


class Orders(models.Model):
    id = models.AutoField(primary_key=True)
    customer = models.ForeignKey('Customer', verbose_name='Заказчик', related_name='orders_customer',
                                 on_delete=models.CASCADE)
    contract_number = models.CharField(verbose_name='Номер договора', max_length=12)
    date_contract = models.DateField(blank=True, null=True,verbose_name='Дата создания договора')
    name = models.ForeignKey('Product', verbose_name='Товар', related_name='orders_product',
                             on_delete=models.CASCADE)
    shipment = models.CharField(verbose_name='Поставка', max_length=120)

    def __str__(self):
        return str(self.id)

    class Meta:
        ordering = ['id']
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'


class Dispatch(models.Model):
    id = models.AutoField(primary_key=True)
    id_orders = models.ForeignKey('Orders', verbose_name='Заказ', related_name='dispatch_orders',
                                  on_delete=models.CASCADE)
    date_shipment = models.DateField(verbose_name='Дата отгрузки',blank=True, null=True)
    dispatch_count = models.CharField(verbose_name='Количество', max_length=120)

    def __str__(self):
        return self.dispatch_count

    class Meta:
        ordering = ['id']
        verbose_name = 'Отгрузка'
        verbose_name_plural = 'Отгрузки'
