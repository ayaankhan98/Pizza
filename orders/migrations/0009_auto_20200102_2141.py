# Generated by Django 3.0.1 on 2020-01-02 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0008_orders'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='size',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
