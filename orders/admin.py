from django.contrib import admin
#from .models import *
# ORDERS
from orders.models import *


class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'customer', 'time_created', 'time_checkout', 'time_delivery']

class OrderProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'order', 'product', 'price', 'quantity']

admin.site.register(Order, OrderAdmin)
admin.site.register(OrderProduct, OrderProductAdmin)