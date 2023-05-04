from django.contrib import admin

# Register your models here.
""" from .models import Peliculas
from .models import Generos
from .models import Artistas
admin.site.register(Artistas)


@admin.register(Peliculas)
class PeliculasAdmin(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'estreno')
    list_per_page = 5
 
@admin.register(Peliculas1)
class PeliculasAdmin1(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'estreno','resumen')
    list_per_page = 5 

@admin.register(Generos)
class PeliculasGeneros(admin.ModelAdmin):
    list_display = ('nombre','id')
    list_per_page = 5  """