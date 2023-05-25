from django.urls import path
from . import views
from . views import PeliculasListView
from . views import PeliculasHomeListView

urlpatterns = [
    path('peliculas_index', views.peliculas_index, name="peliculas_index"),
    #path('', views.index_administracion,name='inicio_administracion'),
    # path('', PeliculasListView.as_view(), name="welcome"),
    path('', views.home_show, name="welcome"),
    path('home', views.home_peliculas, name="home"),
    path('create', views.create, name="create"),

    # path('edit', views.edit, name="edit"),
    path('edit2', views.edit2, name="edit2"),

    # path('listar_peliculas', views.listar_peliculas, name="listar_peliculas"),
    # path('alta_pelicula', views.alta_pelicula, name="alta_pelicula"),


    path('generos/index', views.generos_index,name='generos_index'),
    path('generos/nuevo', views.generos_nuevo,name='generos_nuevo'),
    path('generos/editar/<int:id_genero>', views.generos_editar,name='generos_editar'),
    path('generos/eliminar/<int:id_genero>', views.generos_eliminar,name='generos_eliminar'),
]
