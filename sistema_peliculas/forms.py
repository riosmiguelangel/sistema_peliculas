from xml.dom import ValidationErr
from django import forms
from peliculas.models import Generos
from peliculas.models import Artistas
from peliculas.models import Peliculas
from PIL import Image

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column

class EditForm(forms.Form):
    
    titulo = forms.CharField(
            label='Titulo', 
            max_length=255,
            widget=forms.TextInput(
                    attrs={'class':'form-control','placeholder':'Ingrese titulo de la pelicula', 'rows' : '4'}
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

    # artista1 = forms.ModelChoiceField(
    #     label='Protagonista 1',
    #     queryset=Artistas.objects.all(),
    #     widget=forms.Select(attrs={'class':'form-control'}),
    #     initial='Seleccione una opcion'
    # )
    

    # artista2 = forms.ModelChoiceField(
    #     label='Protagonista 2',
    #     queryset=Artistas.objects.all(),
    #     widget=forms.Select(attrs={'class':'form-control'}),
    #     initial='Seleccione una opcion'
    # )
   
    # artista3 = forms.ModelChoiceField(
    #     label='Protagonista 3',
    #     queryset=Artistas.objects.all(),
    #     widget=forms.Select(attrs={'class':'form-control'}), 
    #     initial='Seleccione una opcion'
    # )


    resumen = forms.CharField(
        label='Resumen',
        max_length=500,
        widget=forms.Textarea(attrs={'rows': 5,'class':'form-control'})
    )

    portada = forms.ImageField(
        label='Portada',    
        max_length=255,
        widget=forms.FileInput(
                    attrs={'class':'btn btn-primary'})
    )

class GeneroForm(forms.ModelForm):
    # nombre = forms.CharField(error_messages={'required':'Hello! no te olvide de mi!'})

    # def clean_nombre(self):
    #     pass
    
    class Meta:
        model=Generos
        # fields='__all__'
        fields=['nombre']
        # exclude=('baja',)
        widgets = {
            'nombre' : forms.TextInput(attrs={'class':'form-control','placeholder':'Ingrese un nombre'})
        }
        error_messages = {
            'nombre' :{
                'required':'No te olvides de mi!'
            }
        }



class AltaPeliculaForm(forms.Form):
    titulo = forms.CharField(
            label='Titulo', 
            max_length=255,
            widget=forms.TextInput(
                    attrs={'class':'form-control','placeholder':'Ingrese titulo de la pelicula', 'rows' : '4'}
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

    """ portada = forms.ImageField(
            label='Portada',    
            max_length=255,
            widget=forms.FileInput(
                        attrs={'class':'btn btn-primary'})
        ) """

    resumen = forms.CharField(
        label='Resumen',
        max_length=500,
        widget=forms.Textarea(attrs={'rows': 5,'class':'form-control'})
    )

    

    def clean(self):
    # Validar si el Alumno a crear ya existe
        if Peliculas.objects.filter(titulo=self.cleaned_data["titulo"]).exists():
            raise ValidationErr("Ya existe un pelicula con ese titulo")

class PeliculaForm(forms.ModelForm):

    titulo=forms.CharField(
            label='Titulo', 
            widget=forms.TextInput(attrs={'class':'form-control'})
        )
    estreno=forms.DateField(
            label='Fecha estreno', 
            widget=forms.DateInput(attrs={'class':'form-control','type':'date'})
        )
    resumen = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 5,'class':'form-control'})
    )
    """Se utiliza ModelChoiceField para poder realizar un filtrado de lo que
    quiero mostrar en el selector"""
    genero = forms.ModelChoiceField(
        queryset=Generos.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    portada = forms.ImageField(
        widget=forms.FileInput(attrs={'class':'form-control'})
    )
    
    class Meta:
        model=Peliculas
        fields=['titulo','estreno','portada','resumen','genero']


class ArtistasForm(forms.ModelForm):
    # nombre = forms.CharField(error_messages={'required':'Hello! no te olvide de mi!'})

    # def clean_nombre(self):
    #     pass
    
    class Meta:
        model=Artistas
        # fields='__all__'
        fields=['nombre']
        # exclude=('baja',)
        widgets = {
            'nombre' : forms.TextInput(attrs={'class':'form-control','placeholder':'Ingrese nombre del artista'})
        }
        error_messages = {
            'nombre' :{
                'required':'No te olvides de mi!'
            }
        }
