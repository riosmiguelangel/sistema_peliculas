from django.urls import path, re_path, include
from . import views

urlpatterns = [
    
    path('index_administracion', views.index_administracion,name='index_administracion'),
    path('generos/index', views.generos_index,name='generos_index'),
    path('generos/nuevo', views.generos_nuevo,name='generos_nuevo'),
    path('generos/editar/<int:id_genero>', views.generos_editar,name='generos_editar'),
    path('generos/eliminar/<int:id_genero>', views.generos_eliminar,name='generos_eliminar'),

    path('artistas/index', views.artistas_index,name='artistas_index'),
    path('artistas/nuevo', views.artistas_nuevo,name='artistas_nuevo'),
    path('artistas/editar/<int:id_artista>', views.artistas_editar,name='artistas_editar'),
    path('artistas/eliminar/<int:id_artista>', views.artistas_eliminar,name='artistas_eliminar'),

    path('peliculas/index', views.peliculas_index,name='peliculas_index'),
    path('peliculas/nueva', views.peliculas_nueva,name='peliculas_nueva'),
    path('peliculas/editar/<int:id_pelicula>', views.peliculas_editar,name='peliculas_editar'),
    path('peliculas/eliminar/<int:id_pelicula>', views.peliculas_eliminar,name='peliculas_eliminar'),
]
