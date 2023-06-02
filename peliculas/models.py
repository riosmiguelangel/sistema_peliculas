from django.db import models
from django.contrib import admin

class Artistas(models.Model):
    nombre = models.CharField(max_length=100,verbose_name='Nombre')

    def __str__(self):
        return self.nombre 

class Generos(models.Model):
    nombre = models.CharField(max_length=150,verbose_name='Nombre')    

    def __str__(self):
        return self.nombre
    
class Plataformas(models.Model):
    nombre = models.CharField(max_length=150,verbose_name='Nombre')    
    icono = models.ImageField(upload_to='imagenes/',null=True,verbose_name='Portada')

    def __str__(self):
        return self.nombre

class Peliculas(models.Model):
    titulo = models.CharField(max_length=128, verbose_name="Titulo")
    genero = models.ForeignKey(Generos,on_delete=models.CASCADE) #relacion mucho a uno    
    estreno = models.CharField(max_length=4,verbose_name='Estreno',null=True,default=None)
    director = models.ForeignKey(Artistas,on_delete=models.CASCADE,related_name='director',default=None)
    artistas = models.ManyToManyField(Artistas,through='Elenco') 
    portada = models.ImageField(upload_to='imagenes/',null=True,verbose_name='Portada')
    resumen = models.TextField(null=True,verbose_name='Resumen')
    plataformas = models.ManyToManyField(Plataformas,through='Donde_ver_pelicula') 

    def __str__(self):
        return self.titulo
   
class Elenco(models.Model):
    pelicula = models.ForeignKey(Peliculas,on_delete=models.CASCADE)
    artista = models.ForeignKey(Artistas,on_delete=models.CASCADE)

    def __str__(self):
        return self.artista.nombre

class Donde_ver_pelicula(models.Model):
    pelicula = models.ForeignKey(Peliculas,on_delete=models.CASCADE)
    plataforma = models.ForeignKey(Plataformas,on_delete=models.CASCADE)

    def __str__(self):
        return self.plataforma.nombre


class ElencoInLine(admin.TabularInline):
    model = Elenco


class Donde_ver_peliculaInLine(admin.TabularInline):
    model = Donde_ver_pelicula

class PeliculasAdmin(admin.ModelAdmin):
    inlines = [
        ElencoInLine,
        Donde_ver_peliculaInLine,
    ]
