# Generated by Django 3.2 on 2021-06-01 07:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='orderproduct',
            options={'verbose_name': 'Order product', 'verbose_name_plural': 'Orders products'},
        ),
        migrations.AlterModelTable(
            name='orderproduct',
            table='orders_products',
        ),
    ]
