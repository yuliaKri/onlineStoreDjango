# Generated by Django 3.2 on 2021-06-11 04:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='token',
            field=models.CharField(default='', max_length=200, verbose_name='Token'),
            preserve_default=False,
        ),
    ]
