# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-04 20:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wiki', '0016_auto_20160804_2207'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemons',
            name='another_img',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='photos/'),
        ),
    ]
