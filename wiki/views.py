#from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.template import loader

from .forms import PokemonForm
from .models import Pokemons

def index_view(request):
	context = { "pokemon_list" : Pokemons.objects.all()}
	template = loader.get_template('wiki/index.html')
	return HttpResponse(template.render(context, request))

def pokemon_list_view(request):
	context = { "pokemon_list" : Pokemons.objects.all()}
	template = loader.get_template('wiki/pokemon_list.html')
	return HttpResponse(template.render(context, request))

def pokemon_view(request, pokedex):
	pokemon = get_object_or_404(Pokemons, pokedex=pokedex)
	template = loader.get_template('wiki/detail.html')
	context = {"pokemon" : pokemon, "pokemon_list" : Pokemons.objects.all()}
	context["previous_exist"], context["next_exist"] = False, False
	context["previous_url"], context["next_url"] = "../{}".format(pokemon.pokedex - 1), "../{}".format(pokemon.pokedex + 1)
	if Pokemons.objects.all().filter(pokedex=int(pokedex)-1):
		context["previous_exist"] = True
	if Pokemons.objects.all().filter(pokedex=int(pokedex)+1):
		context["next_exist"] = True
	return HttpResponse(template.render(context, request))

def edit_view(request, action = None, pokedex = None):
	context = { "pokemon_list": Pokemons.objects.all(),
				"action": action}	
	if request.method == "POST":
		if request.POST.get("button") == "delete":
			context["done"] = True
			Pokemons.objects.filter(pokedex=pokedex)[0].delete()
			return HttpResponseRedirect("/wiki/aoe/edit/")
		if action == "edit":
			f = PokemonForm(request.POST, files = request.FILES, instance = Pokemons.objects.filter(pokedex = pokedex)[0])
			if f.is_valid():
				if (not Pokemons.objects.filter(pokedex = request.POST.get("pokedex")).exists()) or (request.POST.get("pokedex") == pokedex):
					context["done"] = True
					f.save()
					return HttpResponseRedirect("../{}".format(request.POST.get("pokedex")))
				else:
					context["error"] = "This pokedex is occupied."
		elif action == "create":
			f = PokemonForm(request.POST, files = request.FILES)
			if f.is_valid():
				if not Pokemons.objects.filter(pokedex = request.POST.get("pokedex")).exists():
					context["done"] = True
					f.save()
				else:
					context["error"] = "This pokedex is occupied."

	if pokedex:
		context["pokemon"], pokemon = [get_object_or_404(Pokemons, pokedex=pokedex)]*2
		context["previous_exist"], context["next_exist"] = False, False
		context["previous_url"], context["next_url"] = "../{}".format(pokemon.pokedex - 1), "../{}".format(pokemon.pokedex + 1)
		if Pokemons.objects.all().filter(pokedex=int(pokedex)-1):
			context["previous_exist"] = True
		if Pokemons.objects.all().filter(pokedex=int(pokedex)+1):
			context["next_exist"] = True
		form = PokemonForm(instance=pokemon)
		context["form"] = form
	if action == "create":
		form = PokemonForm()
		context["form"] = form

	template = loader.get_template('wiki/pkmn_aoe.html')
	#form = PokemonForm(request.POST)
	#context["form"] = form
	return HttpResponse(template.render(context, request))