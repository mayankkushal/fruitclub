# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-08 19:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fruitclub', '0007_auto_20170209_0124'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productimage',
            name='image',
            field=models.ImageField(null=True, upload_to='product_images'),
        ),
    ]
