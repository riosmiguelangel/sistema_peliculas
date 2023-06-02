from django.contrib import admin

# Register your models here.
from .models import Peliculas
from .models import Generos
from .models import Artistas
from .models import Elenco
from .models import PeliculasAdmin
from .models import Donde_ver_pelicula
from .models import Plataformas
admin.site.register(Artistas)
admin.site.register(Peliculas,PeliculasAdmin)
admin.site.register(Generos)
admin.site.register(Elenco)
admin.site.register(Donde_ver_pelicula)
admin.site.register(Plataformas)


class ArtistasAdmin(admin.ModelAdmin):
    list_display = ('id','nombre')
    list_per_page = 15

class PeliculasAdmin(admin.ModelAdmin):
     list_display = ('id','titulo','estreno')
     list_per_page = 5 

class ElencoAdmin(admin.ModelAdmin):
    list_display = ('id','pelicula', 'artista')
    list_per_page = 5  


class GenerosAdmin(admin.ModelAdmin):
    list_display = ('id','nombre' )
    list_per_page = 5  