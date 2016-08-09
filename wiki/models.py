from django.db import models
from django.conf import settings

class Pokemons(models.Model):
	pokedex = models.IntegerField(default=0, unique=True)
	name = models.CharField(max_length=20)
	evolve_from_at = models.IntegerField(default=0)
	evolve_from_fk = models.ForeignKey("Pokemons", related_name="from_fk", null=True, blank=True, on_delete=models.SET_NULL)
	evolve_to_at = models.IntegerField(default=0)
	evolve_to_fk = models.ForeignKey("Pokemons", related_name="to_fk", null=True, blank=True, on_delete=models.SET_NULL)
	image = models.ImageField(null=True, default=None, blank = True)
	#target = models.ForeignKey(User, related_name='gameclaim_targets')
	#joke (ivysaur/bulbasaur/venusaur: <img>how he should look; if leaves are missing let him out of pokeball for sunlight)
	#pokemon lore
	#pokemon stats
	#pokemon on map
	def __str__(self):
		return self.name
	def get_img(self):
		return self.image.url
	def save(self, **kwargs):
		attributes = ["pokedex", "name", "image", "evolve_from_at", "evolve_from_fk", "evolve_to_at", "evolve_to_fk"]
		before = Change()
		for atr in attributes:
			setattr(before, atr, getattr(self, atr))
		before.save()
		super().save(**kwargs)

class Change(models.Model):
	pokemon = Pokemons()
	time = models.DateTimeField(auto_now_add=True)

	pokedex = models.IntegerField(default=0)
	name = models.CharField(max_length=20)
	evolve_from_at = models.IntegerField(default=0)
	evolve_from_fk = models.ForeignKey("Pokemons", related_name="from_ch", null=True, blank=True, on_delete=models.SET_NULL)
	evolve_to_at = models.IntegerField(default=0)
	evolve_to_fk = models.ForeignKey("Pokemons", related_name="to_ch", null=True, blank=True, on_delete=models.SET_NULL)
	image = models.ImageField(null=True, default=None, blank = True)