from django.contrib import admin

from .models import Pokemons, Pictures

class PokemonsAdmin(admin.ModelAdmin):
	pass
class PicturesAdmin(admin.ModelAdmin):
	pass

admin.site.register(Pokemons, PokemonsAdmin)
admin.site.register(Pictures, PicturesAdmin)