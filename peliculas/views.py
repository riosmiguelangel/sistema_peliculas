from typing import Generic
from django.http import Http404
from django.shortcuts import render, redirect
from administracion.models import Pelicula
from administracion.models import Elenco
from administracion.models import Plataforma
from administracion.models import Donde_ver_pelicula
from administracion.models import Calificacion
from django.contrib.auth.models import User

from peliculas.forms import CalificacionForm

from django.views.generic import ListView

from peliculas.form import RegistrarUsuarioForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LogoutView
from django.contrib.auth import authenticate, login, logout




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

def pelicula_registrarse(request):
    if request.method == 'POST':
        form = RegistrarUsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            messages.success(
                request, f'Tu cuenta fue creada con éxito! Ya te podes loguear en el sistema.')
            return redirect('login')
    else:
        form = RegistrarUsuarioForm()
    return render(request, 'peliculas/registrarse.html', {'form': form, 'title': 'registrese aquí'})

class peliculas_LogoutView(LogoutView):
    # next_page = 'inicio'

    def dispatch(self, request, *args, **kwargs):
        response = super().dispatch(request, *args, **kwargs)
        messages.add_message(request, messages.INFO, 'Se ha cerrado la session correctamente.')
        return response
    

def home_peliculas(request):
    peliculas = Pelicula.objects.all()
    artistas = Elenco.objects.all()
    plataformas = Donde_ver_pelicula.objects.all()
    ver_plataformas = Plataforma.objects.all()
    
    return render(request, 'peliculas/home.html', {'peliculas':peliculas, 'artistas':artistas, 'plataformas':plataformas, 'ver_plataformas':ver_plataformas})



def detalle_pelicula(request):
    #queryset
    # peliculas = Peliculas.objects.all()
    # return render(request,'peliculas/detalle_pelicula.html',{'peliculas':peliculas})

    try:
        pelicula = Pelicula.objects.get(pk=id)
    except Pelicula.DoesNotExist:
        return render(request,'administracion/404_admin.html')    
   
    return render(request,'peliculas/detalle_pelicula.html',{'pelicula':pelicula})

def detalle(request,id_pelicula):
    artistas = Elenco.objects.all()
    plataformas = Donde_ver_pelicula.objects.all()
    #puntajes = Calificacion.objects.all()
    #usuario = User.objects.all()
    try:
        pelicula = Pelicula.objects.get(pk=id_pelicula)
        #usuario = User.objects.get(pk=User.id)
        calificar(request,id_pelicula)
    except Pelicula.DoesNotExist:
        return render(request,'administracion/404_admin.html')

    return render(request, 'peliculas/detalle.html', {'pelicula':pelicula, 'artistas':artistas, 'plataformas':plataformas})

"""
Calificacion estresllas
"""
# def calificar(request):
#     if(request.method=='POST'):
#         formulario = CalificacionForm(request.POST)
#         if formulario.is_valid():
#             formulario.save()
#             return redirect('home')
#     else:
#         formulario = CalificacionForm()
#     return render(request,'administracion/generos/nuevo.html',{'form':formulario})
def calificar(request,id_pelicula):
        if(request.method=='POST'):
            
            if request.method =="POST":
                puntos = request.POST["calificacion"]
                pelicula = request.POST["calificacion"]
                usuario = request.POST["calificacion"]
                calificacion = Calificacion(puntaje= puntos, pelicula= id_pelicula)  
                
                calificacion.save() 
            return render(request,'peliculas/detalle.html')
        else:
            
            return render(request,'peliculas/home.html')