from django.contrib import admin

# Register your models here.
from administracion.models import Pelicula, Genero,Artista,Elenco,PeliculasAdmin,Donde_ver_pelicula,Plataforma, Calificacion
from django.contrib.auth.models import Group,User
from django.contrib.auth.admin import GroupAdmin, UserAdmin



class PersonalizadoAdminSite(admin.AdminSite):
    site_header = 'Administracion Sistema Peliculas'
    site_title = 'Administracion superuser'
    index_title= 'Administracion del sitio'
    empty_value_display = 'No hay datos para visualizar'

# @admin.register(Pelicula)
# class PeliculasAdmin(admin.ModelAdmin):
#     list_display = ('id','titulo','estreno')
#     #list_filter = ('titulo')
#     list_per_page = 5
     

class ArtistaAdmin(admin.ModelAdmin):
    list_display = ('id','nombre')
    list_per_page = 15
    

class GeneroAdmin(admin.ModelAdmin):
    list_display = ('id','nombre' )
    list_per_page = 5  


class CalificacionAdmin(admin.ModelAdmin):
    list_display = ('id','puntaje','pelicula', 'usuario' )
    list_filter = ['puntaje','pelicula', 'usuario']
    list_per_page = 5  

class ElencoAdmin(admin.ModelAdmin):
    list_display = ('id','artista','pelicula' )
    list_filter = ['pelicula','artista']
    list_per_page = 5  

class ElencoInLine(admin.TabularInline):
    model = Elenco 

class Donde_ver_peliculaAdmin(admin.ModelAdmin):
    list_display = ('id','pelicula', 'plataforma' )
    list_filter = ['pelicula', 'plataforma' ]
    list_per_page = 5  


class Donde_ver_peliculaInLine(admin.TabularInline):
    model = Donde_ver_pelicula

class PeliculasAdmin(admin.ModelAdmin):
    list_display = ('id','titulo','estreno','genero')
    list_filter = ['genero', 'director']
    list_per_page = 5
    inlines = [
        ElencoInLine,
        Donde_ver_peliculaInLine,
    ]


sitio_admin = PersonalizadoAdminSite(name="personalizado")
sitio_admin.register(Pelicula,PeliculasAdmin)
sitio_admin.register(Artista, ArtistaAdmin)
sitio_admin.register(Genero,GeneroAdmin)
sitio_admin.register(Elenco,ElencoAdmin)
sitio_admin.register(Donde_ver_pelicula, Donde_ver_peliculaAdmin)
sitio_admin.register(Plataforma)
sitio_admin.register(Calificacion, CalificacionAdmin)
sitio_admin.register(Group, GroupAdmin)
sitio_admin.register(User,UserAdmin)
