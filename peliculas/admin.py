from django.contrib import admin

# Register your models here.
from .models import Peliculas
from .models import Generos
from .models import Artistas

#admin.site.register(Peliculas)
admin.site.register(Generos)
admin.site.register(Artistas)
@admin.register(Peliculas)
class PeliculasAdmin(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'estreno','id_genero','director')
    list_per_page = 5
