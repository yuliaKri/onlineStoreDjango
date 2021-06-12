from django.db import models

# Create your models here.

class Customer(models.Model):
    class Meta:
        db_table = 'customers'
        verbose_name = 'Customer'
        verbose_name_plural = 'Customers'

    first_name = models.CharField(null=True, blank=True, max_length=200, verbose_name='First name')
    last_name = models.CharField(null=True, blank=True, max_length=200, verbose_name='Last name')
    phone = models.BigIntegerField(null=True, blank=True, verbose_name='Phone')
    email = models.CharField(max_length=200, null=True, blank=True, verbose_name='Email')
    time_created = models.DateTimeField(auto_now_add=True, verbose_name='Time created')
    token = models.CharField(null=False, blank=False, max_length=200, verbose_name='Token') # id not jwt

    def __str__(self):
        return self.email


class CustomerAddress(models.Model):
    class Meta:
        db_table = 'customers address'
        verbose_name = 'Customer address'
        verbose_name_plural = 'Customers addresses'

    customer = models.ForeignKey(Customer, null=False, blank=False, verbose_name='Customer', on_delete=models.CASCADE)
    country = models.CharField(null=False, blank=False, max_length=200, verbose_name='Country')
    city = models.CharField(null=False, blank=False, max_length=200, verbose_name='City')
    post_code = models.CharField(null=False, blank=False, max_length=200, verbose_name='Post code')
    address = models.CharField(null=False, blank=False, max_length=200, verbose_name='Address')