from django import forms
from peliculas.models import Generos
from peliculas.models import Artistas
from PIL import Image

class EditForm(forms.Form):
    
    titulo = forms.CharField(
            label='Titulo', 
            max_length=255,
            widget=forms.TextInput(
                    attrs={'class':'form-control','placeholder':'Ingrese titulo de la pelicula'}
            )
        )
    
    estreno = forms.IntegerField(
        label='Año_estreno',
        max_value=2200,
        min_value=1900,
    )

    genero = forms.ModelChoiceField(
        label='Genero',
        queryset=Generos.objects.all(),
        widget=forms.Select(attrs={'class':'form-control'}),
        initial='Seleccione una opcion'
    )

    director = forms.ModelChoiceField(
        label='Director',
        queryset=Artistas.objects.all(),
        widget=forms.Select(attrs={'class':'form-control'}),
        initial='Seleccione una opcion'
    )

    artista1 = forms.ModelChoiceField(
        label='Protagonista 1',
        queryset=Artistas.objects.all(),
        widget=forms.Select(attrs={'class':'form-control'}),
        initial='Seleccione una opcion'
    )
    

    artista2 = forms.ModelChoiceField(
        label='Protagonista 2',
        queryset=Artistas.objects.all(),
        widget=forms.Select(attrs={'class':'form-control'}),
        initial='Seleccione una opcion'
    )
   
    artista3 = forms.ModelChoiceField(
        label='Protagonista 3',
        queryset=Artistas.objects.all(),
        widget=forms.Select(attrs={'class':'form-control'}), 
        initial='Seleccione una opcion'
    )


    resumen = forms.CharField(
        label='Resumen',
        max_length=500,
        widget=forms.Textarea(attrs={'rows': 5,'class':'form-control'})
    )

    portada = forms.ImageField(
        label='Portada',    
        max_length=255,
        widget=forms.FileInput(
                    attrs={'class':'btn btn-primary'}
    )
    )

  