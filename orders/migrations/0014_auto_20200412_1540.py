# Generated by Django 3.0.5 on 2020-04-12 07:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0013_auto_20200411_1750'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='activeorders',
            options={'verbose_name_plural': '1. Active Orders for Fulfillment'},
        ),
        migrations.AlterModelOptions(
            name='dinnerplatter',
            options={'verbose_name_plural': '9. Dinner Platter'},
        ),
        migrations.AlterModelOptions(
            name='orders',
            options={'verbose_name_plural': '2. Cart Items'},
        ),
        migrations.AlterModelOptions(
            name='pasta',
            options={'verbose_name_plural': '7. Pasta'},
        ),
        migrations.AlterModelOptions(
            name='pizzatopping',
            options={'verbose_name_plural': '3. Pizza Toppings'},
        ),
        migrations.AlterModelOptions(
            name='regularpizza',
            options={'verbose_name_plural': '4. Regular Pizza'},
        ),
        migrations.AlterModelOptions(
            name='salad',
            options={'verbose_name_plural': '8. Salad'},
        ),
        migrations.AlterModelOptions(
            name='sicilianpizza',
            options={'verbose_name_plural': '5. Sicilian Pizza'},
        ),
        migrations.AlterModelOptions(
            name='sub',
            options={'verbose_name_plural': '6. Subs'},
        ),
    ]
