from django.db import models
from customers.models import Customer, CustomerAddress
from products.models import Product

# Create your models here.

class Order(models.Model):
    class Meta:
        db_table = 'orders'
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'

    customer = models.ForeignKey(Customer, null=False, blank=False, verbose_name='Customer', on_delete=models.CASCADE)
    customer_shipping_address = models.ForeignKey(CustomerAddress, null=True, blank=False, verbose_name='Shipping address', on_delete=models.CASCADE)
    time_created = models.DateTimeField(auto_now_add=True, verbose_name='Time created')
    time_checkout = models.DateTimeField(null=True, blank=True, verbose_name='Time checkout')
    time_delivery = models.DateTimeField(null=True, blank=True, verbose_name='Time delivery')

    def __str__(self):
        return self.id


class OrderProduct(models.Model):
    class Meta:
        db_table = 'orders_products'
        verbose_name = 'Order product'
        verbose_name_plural = 'Orders products'

    order = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name='Order')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Product')
    price = models.DecimalField(default=0, max_digits=9, decimal_places=2, null=False, blank=False,
                                verbose_name='Price')
    quantity = models.IntegerField(default=1, null=False, blank=False, verbose_name='Quantity')

    #def __str__(self):
    #    return f"Tag for {self.post}: {self.tag}"