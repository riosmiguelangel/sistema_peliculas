from django.shortcuts import render
from peliculas.models import Peliculas
from peliculas.models import Generos
from peliculas.models import Artistas
from django.views.generic import ListView

from sistema_peliculas.forms import EditForm
from django.contrib import messages


# Create your views here.
def index(request):
    
    lista_peliculas = Peliculas.objects.all() , Generos.objects.all()
    lista_generos = Generos.objects.all()
    #lista_peliculas = Generos.objects.all()

    context={
            'lista_peliculas' : lista_peliculas,
            #'lista_generos' : lista_generos,
            #'lista_peliculas' : lista_peliculas,
           
            }
    #return render(request, 'peliculas/welcome.html', context)

class PeliculasListView(ListView):
    model=Peliculas
    template_name = 'peliculas/welcome.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    

class PeliculasHomeListView(ListView):
    model = Peliculas
    template_name = 'peliculas/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


def create(request):
        generos = Generos.objects.all(),
        artistas = Artistas.objects.all(),

        context={
        'listado_generos' : generos,
        # 'artistas' : artistas,
    }
        return render(request, 'peliculas/create.html', context)
   

def store():
    pass


def destroy(request):
        # $pelicula->delete();
        # return redirect()->route('home')
    return render(request, 'peliculas/home.html')
    


def edit(request):
    generos = Generos.objects.all(),
    peliculas = Peliculas.objects.all(),
    artistas = Artistas.objects.all(),

    context={
        'generos' : generos,
        'peliculas' : peliculas,
        'artistas' : artistas
    }

    # return view('peliculas.edit', compact('artistas', 'pelicula', 'generos'));
    return render(request, 'peliculas/edit.html', context)

def edit2(request):
   
    if(request.method=='POST'):
        edit_form = EditForm(request.POST)
        if(edit_form.is_valid()):  
           pelicula = Peliculas()
           
           pelicula.titulo = edit_form.cleaned_data["titulo"]
           pelicula.id_genero = edit_form.cleaned_data["genero"]
           pelicula.estreno = edit_form.cleaned_data["estreno"]
           pelicula.resumen = edit_form.cleaned_data["resumen"]
           pelicula.director = edit_form.cleaned_data["director"]
           pelicula.id_artista1 = edit_form.cleaned_data["id_artista1"]
           pelicula.id_artista2 = edit_form.cleaned_data["id_artista2"]
           pelicula.id_artista3 = edit_form.cleaned_data["id_artista3"]
           pelicula.portada = edit_form.cleaned_data["portada"]

           pelicula.save()
            
            # acción para tomar los datos del formulario            
        else:
            messages.warning(request,'Por favor revisa los campos')
    else:
        edit_form = EditForm()
   
    return render(request, 'peliculas/edit2.html', { "edit_form" : edit_form })


def nada():
     pass


def buscador(Request):
    
    """ $busca = trim($request->busca);
    $tipobus = $request->tipobus;

    if ($tipobus == 1) {
        $sql = Pelicula::where('titulo', 'LIKE', '%' . $busca . '%')->get();
    } else {
        $sql = Artista::where('nombre', 'LIKE', '%' . $busca . '%')->get();
    }

    $cant = $sql->count();

    return view('peliculas.buscador', compact('sql', 'tipobus', 'cant')); """
    return render(Request, 'peliculas/buscador.html')