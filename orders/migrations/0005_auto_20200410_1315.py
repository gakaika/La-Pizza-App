# Generated by Django 3.0.5 on 2020-04-10 05:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_auto_20200410_1246'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='dinnerplatter',
            options={'verbose_name_plural': '7. Dinner Platter'},
        ),
        migrations.AlterModelOptions(
            name='pasta',
            options={'verbose_name_plural': '5. Pasta'},
        ),
        migrations.AlterModelOptions(
            name='salad',
            options={'verbose_name_plural': '6. Salad'},
        ),
        migrations.AlterModelOptions(
            name='sub',
            options={'verbose_name_plural': '4. Subs'},
        ),
    ]
