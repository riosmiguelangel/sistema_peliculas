from django.contrib import admin

# Register your models here.
from .models import Peliculas
from .models import Generos
from .models import Artistas
from .models import Elenco
# admin.site.register(Artistas)
# admin.site.register(Peliculas)
# admin.site.register(Generos)
# admin.site.register(Elenco)



@admin.register(Artistas)
class PeliculasArtistas(admin.ModelAdmin):
    list_display = ('id','nombre')
    list_per_page = 15


@admin.register(Peliculas)
class PeliculasAdmin(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'estreno')
    list_per_page = 5
 
"""@admin.register(Peliculas1)
class PeliculasAdmin1(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'estreno','resumen')
    list_per_page = 5 """

@admin.register(Elenco)
class PeliculasElenco(admin.ModelAdmin):
    list_display = ('id','pelicula', 'artista')
    list_per_page = 5  


@admin.register(Generos)
class PeliculasGeneros(admin.ModelAdmin):
    list_display = ('id','nombre' )
    list_per_page = 5  