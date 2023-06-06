from django.urls import path,re_path,include
from . import views

urlpatterns = [
    path('peliculas_index', views.peliculas_index, name="peliculas_index"),
    path('', views.home_show, name="welcome"),
    path('home', views.home_peliculas, name="home"),
    path('create', views.create, name="create"),

    path('edit', views.edit, name="edit"),
    # path('detalle_pelicula/<int:id_pelicula>', views.detalle_pelicula, name="detalle_pelicula"),

]
