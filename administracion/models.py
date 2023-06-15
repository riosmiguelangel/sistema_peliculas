from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User

class Artista(models.Model):
    nombre = models.CharField(max_length=100,verbose_name='Nombre')

    def __str__(self):
        return self.nombre 

class Genero(models.Model):
    nombre = models.CharField(max_length=150,verbose_name='Nombre')    

    def __str__(self):
        return self.nombre
    
class Plataforma(models.Model):
    nombre = models.CharField(max_length=150,verbose_name='Nombre')    
    icono = models.ImageField(upload_to='imagenes/',null=True,verbose_name='Portada')

    def __str__(self):
        return self.nombre

class Pelicula(models.Model):
    titulo = models.CharField(max_length=128, verbose_name="Titulo")
    genero = models.ForeignKey(Genero,on_delete=models.CASCADE) #relacion mucho a uno    
    estreno = models.CharField(max_length=4,verbose_name='Estreno',null=True,default=None)
    director = models.ForeignKey(Artista,on_delete=models.CASCADE,related_name='director',default=None)
    artistas = models.ManyToManyField(Artista,through='Elenco') 
    portada = models.ImageField(upload_to='imagenes/',null=True,verbose_name='Portada')
    portada_grande = models.ImageField(upload_to='imagenes/',null=True,verbose_name='Portada_grande')
    resumen = models.TextField(null=True,verbose_name='Resumen')
    plataformas = models.ManyToManyField(Plataforma,through='Donde_ver_pelicula') 

    def __str__(self):
        return self.titulo
   
class Elenco(models.Model):
    pelicula = models.ForeignKey(Pelicula,on_delete=models.CASCADE)
    artista = models.ForeignKey(Artista,on_delete=models.CASCADE)

    def __str__(self):
        return self.artista.nombre

class Donde_ver_pelicula(models.Model):
    pelicula = models.ForeignKey(Pelicula,on_delete=models.CASCADE)
    plataforma = models.ForeignKey(Plataforma,on_delete=models.CASCADE)

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


class Calificacion(models.Model):
    pelicula = models.ForeignKey(Pelicula,on_delete=models.CASCADE)
    puntaje = models.IntegerField(max_length=1, verbose_name="puntaje")
    usuario = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.usuario, self.puntaje,self.pelicula
    
    