# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-04 19:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wiki', '0012_auto_20160801_2234'),
    ]

    operations = [
        migrations.AddField(
            model_name='pokemons',
            name='another_img',
            field=models.FileField(default=None, null=True, upload_to=''),
        ),
    ]
