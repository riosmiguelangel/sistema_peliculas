from django.contrib import admin

# Register your models here.
from administracion.models import Pelicula, Genero,Artista,Elenco,PeliculasAdmin,Donde_ver_pelicula,Plataforma

admin.site.register(Artista)
admin.site.register(Pelicula,PeliculasAdmin)
admin.site.register(Genero)
admin.site.register(Elenco)
admin.site.register(Donde_ver_pelicula)
admin.site.register(Plataforma)


class ArtistaAdmin(admin.ModelAdmin):
    list_display = ('id','nombre')
    list_per_page = 15

class PeliculaAdmin(admin.ModelAdmin):
     list_display = ('id','titulo','estreno')
     list_filter = 'titulo'
     list_per_page = 5 

class ElencoAdmin(admin.ModelAdmin):
    list_display = ('id','pelicula', 'artista')
    list_per_page = 5  


class GeneroAdmin(admin.ModelAdmin):
    list_display = ('id','nombre' )
    list_per_page = 5  