from django.contrib import admin

# Register your models here.
from administracion.models import Pelicula, Genero,Artista,Elenco,PeliculasAdmin,Donde_ver_pelicula,Plataforma
from django.contrib.auth.models import Group,User
from django.contrib.auth.admin import GroupAdmin, UserAdmin

class PersonalizadoAdminSite(admin.AdminSite):
    site_header = 'Administracion Sistema Peliculas'
    site_title = 'Administracion superuser'
    index_title= 'Administracion del sitio'
    empty_value_display = 'No hay datos para visualizar'


class PeliculasAdmin(admin.ModelAdmin):
     list_display = ('id','titulo','estreno')
     list_filter = 'titulo'
     list_per_page = 5

class ArtistaAdmin(admin.ModelAdmin):
    list_display = ('id','nombre')
    list_per_page = 15

 
class GeneroAdmin(admin.ModelAdmin):
    list_display = ('id','nombre' )
    list_per_page = 5  



class ElencoInLine(admin.TabularInline):
    model = Elenco


class Donde_ver_peliculaInLine(admin.TabularInline):
    model = Donde_ver_pelicula

class PeliculasAdmin(admin.ModelAdmin):
    inlines = [
        ElencoInLine,
        Donde_ver_peliculaInLine,
    ]

sitio_admin = PersonalizadoAdminSite(name="personalizado")
sitio_admin.register(Pelicula,PeliculasAdmin)
sitio_admin.register(Artista)
sitio_admin.register(Genero)
sitio_admin.register(Elenco)
sitio_admin.register(Donde_ver_pelicula)
sitio_admin.register(Plataforma)
sitio_admin.register(Group, GroupAdmin)
sitio_admin.register(User,UserAdmin)