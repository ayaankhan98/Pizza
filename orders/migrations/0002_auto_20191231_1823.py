# Generated by Django 3.0.1 on 2019-12-31 12:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='toppings',
            old_name='toppingname',
            new_name='topping',
        ),
    ]