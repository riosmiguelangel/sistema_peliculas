from django.shortcuts import render
from peliculas.models import Peliculas
from peliculas.models import Generos

# Create your views here.
def index(request):

    lista_peliculas = Peliculas.objects.all()

    context={
            'listado_peliculas' : lista_peliculas,
            'lista_peliculas' : lista_peliculas,
            }
    return render(request, 'peliculas/welcome.html', context)
           
