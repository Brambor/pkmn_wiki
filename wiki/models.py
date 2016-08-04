from django.db import models
from django.conf import settings

class Pokemons(models.Model):
	pokedex = models.IntegerField(default=0)
	pokemon_name = models.CharField(max_length=20)
	pokemon_img = models.CharField(max_length=24)
	evolve_from_at = models.IntegerField(default=0)
	evolve_from_fk = models.ForeignKey("Pokemons", related_name="from_fk", null=True, blank=True)
	evolve_to_at = models.IntegerField(default=0)
	evolve_to_fk = models.ForeignKey("Pokemons", related_name="to_fk", null=True, blank=True)
	another_img = models.ImageField(null=True, default=None, blank = True)
	#target = models.ForeignKey(User, related_name='gameclaim_targets')
	#joke (ivysaur/bulbasaur/venusaur: <img>how he should look; if leaves are missing let him out of pokeball for sunlight)
	#pokemon lore
	#pokemon stats
	#pokemon on map
	def __str__(self):
		return self.pokemon_name
	def get_img(self):
		return "images/{}".format(self.pokemon_img)