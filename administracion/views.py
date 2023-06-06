from typing import Generic
from django.http import Http404
from django.shortcuts import render, redirect
from administracion.models import Pelicula
from administracion.models import Genero
from administracion.models import Artista
from administracion.models import Elenco
from administracion.models import Plataforma
from administracion.models import Donde_ver_pelicula


from administracion.forms import GeneroForm, ArtistasForm, PeliculaForm
from django.contrib.auth.decorators import login_required


# Create your views here.


def index_administracion(request):
    variable = 'test variable'
    return render(request,'index_administracion.html',{'variable':variable})


"""
    CRUD generos
"""

def generos_index(request):
    #queryset
    generos = Genero.objects.all()
    return render(request,'administracion/generos/index.html',{'generos': generos})

def generos_nuevo(request):
    if(request.method=='POST'):
        formulario = GeneroForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('generos_index')
    else:
        formulario = GeneroForm()
    return render(request,'administracion/generos/nuevo.html',{'form':formulario})

def generos_editar(request,id_genero):
    try:
        genero = Genero.objects.get(pk=id_genero)
    except Genero.DoesNotExist:
        return render(request,'administracion/404_admin.html')

    if(request.method=='POST'):
        formulario = GeneroForm(request.POST,instance=genero)
        if formulario.is_valid():
            formulario.save()
            return redirect('generos_index')
    else:
        formulario = GeneroForm(instance=genero)
    return render(request,'administracion/generos/editar.html',{'form':formulario})

def generos_eliminar(request,id_genero):
    try:
        genero = Genero.objects.get(pk=id_genero)
    except Genero.DoesNotExist:
        return render(request,'administracion/404_admin.html')    
    genero.delete()
    return redirect('generos_index')

"""
    CRUD artistas
"""
def artistas_index(request):
    #queryset
    artistas = Artista.objects.all()
    return render(request,'administracion/artistas/index.html',{'artistas': artistas})

def artistas_nuevo(request):
    if(request.method=='POST'):
        formulario = ArtistasForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('artistas_index')
    else:
        formulario = ArtistasForm()
    return render(request,'administracion/artistas/nuevo.html',{'form':formulario})

def artistas_editar(request,id_artista):
    try:
        artista = Artista.objects.get(pk=id_artista)
    except Artista.DoesNotExist:
        return render(request,'administracion/404_admin.html')

    if(request.method=='POST'):
        formulario = ArtistasForm(request.POST,instance=artista)
        if formulario.is_valid():
            formulario.save()
            return redirect('artistas_index')
    else:
        formulario = ArtistasForm(instance=artista)
    return render(request,'administracion/artistas/editar.html',{'form':formulario})

def artistas_eliminar(request,id_artista):
    try:
        artista = Artista.objects.get(pk=id_artista)
    except Artista.DoesNotExist:
        return render(request,'administracion/404_admin.html')    
    artista.delete()
    return redirect('artistas_index')

"""
    CRUD peliculas
"""
def peliculas_index(request):
    #queryset
    peliculas = Pelicula.objects.all()
    return render(request,'administracion/peliculas/index.html',{'peliculas': peliculas})

def peliculas_nueva(request):
    if(request.method=='POST'):
        formulario = PeliculaForm(request.POST,request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect('peliculas_index')
    else:
        formulario = PeliculaForm()
    return render(request,'administracion/peliculas/nueva.html',{'form':formulario})

def peliculas_editar(request,id_pelicula):
    try:
        pelicula = Pelicula.objects.get(pk=id_pelicula)
    except Pelicula.DoesNotExist:
        return render(request,'administracion/404_admin.html')

    if(request.method=='POST'):
        formulario = PeliculaForm(request.POST,instance=pelicula)
        if formulario.is_valid():
            formulario.save()
            return redirect('peliculas_index')
    else:
        formulario = PeliculaForm(instance=pelicula)
    return render(request,'administracion/peliculas/editar.html',{'form':formulario})

def peliculas_eliminar(request,id_pelicula):
    try:
       pelicula = Pelicula.objects.get(pk=id_pelicula)
    except Pelicula.DoesNotExist:
        return render(request,'administracion/404_admin.html')    
    pelicula.delete()
    return redirect('peliculas_index')





