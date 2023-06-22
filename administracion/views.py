from typing import Generic
from django.http import Http404
from django.shortcuts import render, redirect
from administracion.models import Pelicula
from administracion.models import Genero
from administracion.models import Artista
from administracion.models import Elenco
from administracion.models import Plataforma
from administracion.models import Donde_ver_pelicula
from administracion.models import Calificacion

from administracion.forms import GeneroForm, ArtistasForm, PeliculaForm, PlataformaForm
from django.contrib.auth.decorators import login_required


# Create your views here.

@login_required
def index_administracion(request):
    variable = 'test variable'
    return render(request,'administracion/index_administracion.html',{'variable':variable})


"""
    CRUD generos
"""
@login_required
def generos_index(request):
    #queryset
    generos = Genero.objects.all()
    return render(request,'administracion/generos/index.html',{'generos': generos})

@login_required
def generos_nuevo(request):
    if(request.method=='POST'):
        formulario = GeneroForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('generos_index')
    else:
        formulario = GeneroForm()
    return render(request,'administracion/generos/nuevo.html',{'form':formulario})

@login_required
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

@login_required
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

@login_required
def artistas_index(request):
    #queryset
    artistas = Artista.objects.all()
    return render(request,'administracion/artistas/index.html',{'artistas': artistas})

@login_required
def artistas_nuevo(request):
    if(request.method=='POST'):
        formulario = ArtistasForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('artistas_index')
    else:
        formulario = ArtistasForm()
    return render(request,'administracion/artistas/nuevo.html',{'form':formulario})

@login_required
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

@login_required
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
@login_required
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

@login_required
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

@login_required
def peliculas_eliminar(request,id_pelicula):
    try:
       pelicula = Pelicula.objects.get(pk=id_pelicula)
    except Pelicula.DoesNotExist:
        return render(request,'administracion/404_admin.html')    
    pelicula.delete()
    return redirect('peliculas_index')

"""
    CRUD plataformas
"""
@login_required
def plataformas_index(request):
    #queryset
    plataformas = Plataforma.objects.all()
    return render(request,'administracion/plataformas/index.html',{'plataformas': plataformas})

@login_required
def plataformas_nuevo(request):
    if(request.method=='POST'):
        formulario = PlataformaForm(request.POST, request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect('plataformas_index')
    else:
        formulario = PlataformaForm()
    return render(request,'administracion/plataformas/nuevo.html',{'form':formulario})

@login_required
def plataformas_editar(request,id_plataforma):
    try:
        plataforma = Plataforma.objects.get(pk=id_plataforma)
    except Plataforma.DoesNotExist:
        return render(request,'administracion/404_admin.html')

    if(request.method=='POST'):
        formulario = PlataformaForm(request.POST,instance=plataforma)
        if formulario.is_valid():
            formulario.save()
            return redirect('plataformas_index')
    else:
        formulario = PlataformaForm(instance=plataforma)
    return render(request,'administracion/plataformas/editar.html',{'form':formulario})

@login_required
def plataformas_eliminar(request,id_plataforma):
    try:
        plataforma = Plataforma.objects.get(pk=id_plataforma)
    except Plataforma.DoesNotExist:
        return render(request,'administracion/404_admin.html')    
    plataforma.delete()
    return redirect('plataformas_index')







