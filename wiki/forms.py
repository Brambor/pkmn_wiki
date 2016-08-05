from django import forms
from django.forms import ModelForm

from .models import Pokemons

class PokemonForm(ModelForm):
	class Meta:
		model = Pokemons
		fields = ["pokedex", "pokemon_name", "image", "evolve_from_at", "evolve_from_fk", "evolve_to_at", "evolve_to_fk"]