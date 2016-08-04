from django.conf.urls import url

from . import views

from django.conf import settings
from django.conf.urls.static import static

app_name = 'wiki'
urlpatterns = [
    url(r'^$', views.index_view),
    url(r'^pokemons/$', views.pokemon_list_view),
    url(r'^pokemons/(?P<pokedex>[0-9]+)/$', views.pokemon_view),
    url(r'^aoe/$', views.edit_view),
    url(r'^aoe/(?P<action>\w+)/$', views.edit_view),
    url(r'^aoe/(?P<action>\w+)/(?P<pokedex>[0-9]+)/$', views.edit_view),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)