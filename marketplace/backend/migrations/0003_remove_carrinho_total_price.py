# Generated by Django 3.2.6 on 2021-08-26 23:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0002_carrinho_total_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='carrinho',
            name='total_price',
        ),
    ]
