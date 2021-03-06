# Generated by Django 3.0.2 on 2020-01-16 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0013_auto_20200116_0940'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='item',
            field=models.CharField(blank=True, max_length=64),
        ),
        migrations.AddField(
            model_name='orders',
            name='item_id',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='orders',
            name='payment',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='orders',
            name='quantity',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='orders',
            name='size',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
