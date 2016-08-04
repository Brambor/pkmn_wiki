# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-01 09:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wiki', '0007_auto_20160801_1132'),
    ]

    operations = [
        migrations.AddField(
            model_name='pokemons',
            name='evolve_from_fk',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='from_fk', to='wiki.Pokemons'),
        ),
        migrations.AddField(
            model_name='pokemons',
            name='evolve_to_fk',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='to_fk', to='wiki.Pokemons'),
        ),
    ]
