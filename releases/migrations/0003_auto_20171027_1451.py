# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-10-27 13:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('releases', '0002_auto_20171011_1546'),
    ]

    operations = [
        migrations.AlterField(
            model_name='release',
            name='cover',
            field=models.ImageField(default='missing.gif', upload_to='covers'),
        ),
    ]
