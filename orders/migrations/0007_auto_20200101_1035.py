# Generated by Django 3.0.1 on 2020-01-01 05:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0006_auto_20200101_1035'),
    ]

    operations = [
        migrations.AlterField(
            model_name='regularpizza',
            name='type_of_dish',
            field=models.CharField(choices=[('S', 'Single'), ('M', 'Multiple')], max_length=1),
        ),
        migrations.AlterField(
            model_name='silicianpizza',
            name='type_of_dish',
            field=models.CharField(choices=[('S', 'Single'), ('M', 'Multiple')], max_length=1),
        ),
    ]
