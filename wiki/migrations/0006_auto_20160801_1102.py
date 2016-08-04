# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-01 09:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wiki', '0005_pokemons_evolve_from_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pokemons',
            name='evolve_from',
        ),
        migrations.RemoveField(
            model_name='pokemons',
            name='evolve_from_at',
        ),
        migrations.RemoveField(
            model_name='pokemons',
            name='evolve_from_pokemon',
        ),
        migrations.RemoveField(
            model_name='pokemons',
            name='evolve_to',
        ),
        migrations.RemoveField(
            model_name='pokemons',
            name='evolve_to_at',
        ),
        migrations.RemoveField(
            model_name='pokemons',
            name='evolve_to_pokemon',
        ),
        migrations.AddField(
            model_name='pokemons',
            name='evolve',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='wiki.Pokemons'),
        ),
    ]
