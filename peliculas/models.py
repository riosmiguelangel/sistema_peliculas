from django.db import models

# Create your models here.
class Artistas(models.Model):
    id = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=255)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'artistas'
        
class Generos(models.Model):
    # id_genero= models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255)
   
    class Meta:
        managed = False
        db_table = 'generos'


class Peliculas(models.Model):
    # id= models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=255)
    estreno = models.IntegerField()
    id_genero = models.IntegerField(db_column='Id_genero')  # Field name made lowercase.
    #genero = models.ForeignKey(Generos,null=True, blank=True, on_delete=models.CASCADE)
    director = models.IntegerField(db_column='Id_director')  # Field name made lowercase.
    id_artista1 = models.IntegerField(db_column='Id_artista1')  # Field name made lowercase.
    id_artista2 = models.IntegerField(db_column='Id_artista2')  # Field name made lowercase.
    id_artista3 = models.IntegerField(db_column='Id_artista3')  # Field name made lowercase.
    portada = models.CharField(max_length=255)
    resumen = models.TextField()
    

    class Meta:
        managed = False
        db_table = 'peliculas'

    def __str__(self):
        return self.titulo
    
