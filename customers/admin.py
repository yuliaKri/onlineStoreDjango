from django.contrib import admin
# Register your models here.
from .models import *

class CustomerAdmin(admin.ModelAdmin):
    list_display = ['email', 'token', 'time_created']

class CustomerAddressAdmin(admin.ModelAdmin):
    list_display = ['post_code']

admin.site.register(Customer, CustomerAdmin)
admin.site.register(CustomerAddress, CustomerAddressAdmin)