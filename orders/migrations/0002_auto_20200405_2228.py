# Generated by Django 3.0.5 on 2020-04-05 14:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='PizzaToppings',
            new_name='PizzaTopping',
        ),
        migrations.RenameModel(
            old_name='SubToppings',
            new_name='SubTopping',
        ),
    ]
