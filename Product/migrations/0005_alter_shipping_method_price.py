# Generated by Django 3.2.9 on 2021-11-24 10:41

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0004_auto_20211124_1354'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shipping_method',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10, validators=[django.core.validators.MinValueValidator(0)]),
        ),
    ]
