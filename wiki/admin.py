from django.contrib import admin

from .models import Pokemons

class PokemonsAdmin(admin.ModelAdmin):
	pass

admin.site.register(Pokemons, PokemonsAdmin)