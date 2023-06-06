from typing import Generic
from django.http import Http404
from django.shortcuts import render, redirect
from administracion.models import Pelicula
from administracion.models import Genero
from administracion.models import Artista
from administracion.models import Elenco
from administracion.models import Plataforma
from administracion.models import Donde_ver_pelicula
from django.views.generic import ListView

from administracion.forms import EditForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required



# Create your views here.
class PeliculasListView(ListView):
    model=Pelicula
    context_object_name = 'peliculas'
    template_name = 'peliculas/welcome.html'
    queryset = Pelicula.objects.all()
    ordering = ['titulo']
    paginate_by = 6
   

class PeliculasHomeListView(ListView):
    model = Pelicula
    template_name = 'peliculas/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

def home_show(request):
    peliculas = Pelicula.objects.all()
    plataformas = Plataforma.objects.all()
    artistas = Elenco.objects.all()
    
    return render(request, 'peliculas/welcome.html', {'peliculas':peliculas, 'artistas':artistas, 'plataformas':plataformas})

def home_peliculas(request):
    peliculas = Pelicula.objects.all()
    artistas = Elenco.objects.all()
    plataformas = Donde_ver_pelicula.objects.all()
    
    return render(request, 'peliculas/home.html', {'peliculas':peliculas, 'artistas':artistas, 'plataformas':plataformas})

def create(request):
    generos = Genero.objects.all(),
    artistas = Artista.objects.all(),

    return render(request, 'peliculas/create.html', {'generos':generos, 'artistas':artistas})


def edit(request):
   
    if(request.method=='POST'):
        edit_form = EditForm(request.POST)
        if(edit_form.is_valid()):  
           pelicula = Pelicula()
           
           pelicula.titulo = edit_form.cleaned_data["titulo"]
           pelicula.genero = edit_form.cleaned_data["genero"]
           pelicula.estreno = edit_form.cleaned_data["estreno"]
           pelicula.resumen = edit_form.cleaned_data["resumen"]
           pelicula.director = edit_form.cleaned_data["director"]
           pelicula.portada = edit_form.cleaned_data["portada"]


           pelicula.save()
            
            # acción para tomar los datos del formulario            
        else:
            messages.warning(request,'Por favor revisa los campos')
            messages.add_message(request, messages.WARNING, 'Revisa los campos')
    else:
        edit_form = EditForm()
   
    return render(request, 'peliculas/edit.html', { "edit_form" : edit_form })

def peliculas_index(request):
    #queryset
    peliculas = Pelicula.objects.all()
    return render(request,'peliculas/peliculas_index.html',{'peliculas':peliculas})


def detalle_pelicula(request):
    #queryset
    # peliculas = Peliculas.objects.all()
    # return render(request,'peliculas/detalle_pelicula.html',{'peliculas':peliculas})

    try:
        pelicula = Pelicula.objects.get(pk=id)
    except Pelicula.DoesNotExist:
        return render(request,'administracion/404_admin.html')    
   
    return render(request,'peliculas/detalle_pelicula.html',{'pelicula':pelicula})


