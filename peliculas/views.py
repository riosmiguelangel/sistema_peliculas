from typing import Generic
from django.http import Http404
from django.shortcuts import render, redirect
from peliculas.models import Peliculas
from peliculas.models import Generos
from peliculas.models import Artistas
from peliculas.models import Elenco
from peliculas.models import Plataformas
from peliculas.models import Donde_ver_pelicula
from django.views.generic import ListView

from sistema_peliculas.forms import EditForm, GeneroForm, ArtistasForm
from django.contrib import messages


# Create your views here.
class PeliculasListView(ListView):
    model=Peliculas
    context_object_name = 'peliculas'
    template_name = 'peliculas/welcome.html'
    queryset = Peliculas.objects.all()
    ordering = ['titulo']
    paginate_by = 6
   

class PeliculasHomeListView(ListView):
    model = Peliculas
    template_name = 'peliculas/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

def home_show(request):
    peliculas = Peliculas.objects.all()
    plataformas = Plataformas.objects.all()
    artistas = Elenco.objects.all()
    
    return render(request, 'peliculas/welcome.html', {'peliculas':peliculas, 'artistas':artistas, 'plataformas':plataformas})

def home_peliculas(request):
    peliculas = Peliculas.objects.all()
    artistas = Elenco.objects.all()
    plataformas = Donde_ver_pelicula.objects.all()
    
    return render(request, 'peliculas/home.html', {'peliculas':peliculas, 'artistas':artistas, 'plataformas':plataformas})

def create(request):
    generos = Generos.objects.all(),
    artistas = Artistas.objects.all(),

    return render(request, 'peliculas/create.html', {'generos':generos, 'artistas':artistas})


def edit2(request):
   
    if(request.method=='POST'):
        edit_form = EditForm(request.POST)
        if(edit_form.is_valid()):  
           pelicula = Peliculas()
           
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
   
    return render(request, 'peliculas/edit2.html', { "edit_form" : edit_form })


def index_administracion(request):
    variable = 'test variable'
    return render(request,'peliculas/administracion/index_administracion.html',{'variable':variable})

def peliculas_index(request):
    #queryset
    peliculas = Peliculas.objects.all()
    return render(request,'peliculas/peliculas_index.html',{'peliculas':peliculas})


def detalle_pelicula(request):
    #queryset
    # peliculas = Peliculas.objects.all()
    # return render(request,'peliculas/detalle_pelicula.html',{'peliculas':peliculas})

    try:
        pelicula = Peliculas.objects.get(pk=id)
    except Peliculas.DoesNotExist:
        return render(request,'administracion/404_admin.html')    
   
    return render(request,'peliculas/detalle_pelicula.html',{'pelicula':pelicula})



"""
    CRUD generos
"""

def generos_index(request):
    #queryset
    generos = Generos.objects.all()
    return render(request,'peliculas/administracion/generos/index.html',{'generos': generos})

def generos_nuevo(request):
    if(request.method=='POST'):
        formulario = GeneroForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('generos_index')
    else:
        formulario = GeneroForm()
    return render(request,'peliculas/administracion/generos/nuevo.html',{'form':formulario})

def generos_editar(request,id_genero):
    try:
        genero = Generos.objects.get(pk=id_genero)
    except Generos.DoesNotExist:
        return render(request,'administracion/404_admin.html')

    if(request.method=='POST'):
        formulario = GeneroForm(request.POST,instance=genero)
        if formulario.is_valid():
            formulario.save()
            return redirect('generos_index')
    else:
        formulario = GeneroForm(instance=genero)
    return render(request,'peliculas/administracion/generos/editar.html',{'form':formulario})

def generos_eliminar(request,id_genero):
    try:
        genero = Generos.objects.get(pk=id_genero)
    except Generos.DoesNotExist:
        return render(request,'administracion/404_admin.html')    
    genero.delete()
    return redirect('generos_index')

"""
    CRUD artistas
"""
def artistas_index(request):
    #queryset
    artistas = Artistas.objects.all()
    return render(request,'peliculas/administracion/artistas/index.html',{'artistas': artistas})

def artistas_nuevo(request):
    if(request.method=='POST'):
        formulario = ArtistasForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('artistas_index')
    else:
        formulario = ArtistasForm()
    return render(request,'peliculas/administracion/artistas/nuevo.html',{'form':formulario})

def artistas_editar(request,id_artista):
    try:
        artista = Artistas.objects.get(pk=id_artista)
    except Artistas.DoesNotExist:
        return render(request,'administracion/404_admin.html')

    if(request.method=='POST'):
        formulario = ArtistasForm(request.POST,instance=artista)
        if formulario.is_valid():
            formulario.save()
            return redirect('artistas_index')
    else:
        formulario = ArtistasForm(instance=artista)
    return render(request,'peliculas/administracion/artistas/editar.html',{'form':formulario})

def artistas_eliminar(request,id_artista):
    try:
        artista = Artistas.objects.get(pk=id_artista)
    except Artistas.DoesNotExist:
        return render(request,'administracion/404_admin.html')    
    artista.delete()
    return redirect('artistas_index')

