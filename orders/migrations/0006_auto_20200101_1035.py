# Generated by Django 3.0.1 on 2020-01-01 05:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0005_auto_20200101_1029'),
    ]

    operations = [
        migrations.RenameField(
            model_name='regularpizza',
            old_name='type',
            new_name='type_of_dish',
        ),
        migrations.RenameField(
            model_name='silicianpizza',
            old_name='type',
            new_name='type_of_dish',
        ),
    ]
