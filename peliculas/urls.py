from django.urls import path
from . import views
from . views import PeliculasListView
from . views import PeliculasHomeListView


urlpatterns = [
    #path('', views.index, name="welcome"),
    path('', PeliculasListView.as_view(), name="welcome"),
    path('home', PeliculasHomeListView.as_view(), name="home"),
    path('create', views.create, name="create"),
    path('edit', views.edit, name="edit"),
    path('edit2', views.edit2, name="edit2"),
    path('home', views.destroy, name="home"),
    path('buscador', views.buscador, name="buscador"),
]