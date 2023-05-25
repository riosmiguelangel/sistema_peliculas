# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
class Artistas(models.Model):
    nombre = models.CharField(max_length=100,verbose_name='Nombre')

    def __str__(self):
        return self.nombre 

class Generos(models.Model):
    nombre = models.CharField(max_length=150,verbose_name='Nombre')    

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
   
class Elenco(models.Model):
    pelicula = models.ForeignKey(Peliculas,on_delete=models.CASCADE)
    artista = models.ForeignKey(Artistas,on_delete=models.CASCADE)

    def __str__(self):
        return self.artista.nombre
    
