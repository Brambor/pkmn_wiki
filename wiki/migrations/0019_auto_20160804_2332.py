# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-04 21:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wiki', '0018_auto_20160804_2240'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemons',
            name='another_img',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='C:\\Users\\Tonda_2\\Documents\\Django learning\\pkmn_wiki\\wiki/static/images/'),
        ),
    ]
