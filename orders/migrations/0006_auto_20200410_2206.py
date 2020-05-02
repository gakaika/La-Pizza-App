# Generated by Django 3.0.5 on 2020-04-10 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0005_auto_20200410_1315'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='regularpizza',
            name='toppings',
        ),
        migrations.RemoveField(
            model_name='sicilianpizza',
            name='toppings',
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=256)),
                ('product_type', models.CharField(max_length=64)),
                ('item_type', models.CharField(max_length=64)),
                ('size', models.CharField(blank=True, max_length=64)),
                ('cost', models.FloatField()),
                ('num_toppings', models.PositiveSmallIntegerField(blank=True)),
                ('order_completed', models.BooleanField(default=False)),
                ('pizza_toppings', models.ManyToManyField(blank=True, related_name='pizza_toppings', to='orders.PizzaTopping')),
            ],
        ),
    ]
