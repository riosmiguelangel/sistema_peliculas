from xml.dom import ValidationErr
from django import forms
from .models import Genero, Artista,Pelicula,Calificacion,Plataforma
from django.contrib.auth.models import User
from PIL import Image



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
        queryset=Genero.objects.all(),
        widget=forms.Select(attrs={'class':'form-control'}),
        initial='Seleccione una opcion'
    )

    director = forms.ModelChoiceField(
        label='Director',
        queryset=Artista.objects.all(),
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
                    attrs={'class':'btn btn-primary'})
    )

class GeneroForm(forms.ModelForm):
    # nombre = forms.CharField(error_messages={'required':'Hello! no te olvide de mi!'})

    # def clean_nombre(self):
    #     pass
    
    class Meta:
        model=Genero
        fields=['nombre']
        widgets = {
            'nombre' : forms.TextInput(attrs={'class':'form-control','placeholder':'Ingrese un nombre'})
        }
        error_messages = {
            'nombre' :{
                'required':'No te olvides de mi!'
            }
        }

class PlataformaForm(forms.ModelForm):
    class Meta:
        model=Plataforma
        fields=['nombre','icono']
        widgets = {
            'nombre' : forms.TextInput(attrs={'class':'form-control','placeholder':'Ingrese un nombre'}),
            'icono' : forms.FileInput(attrs={'class':'form-control'}),
        }


class PeliculaForm(forms.ModelForm):

    titulo=forms.CharField(
            label='Titulo', 
            widget=forms.TextInput(attrs={'class':'form-control'})
        )
    estreno=forms.CharField(
            label='Fecha estreno', 
            widget=forms.NumberInput(attrs={'class':'form-control'})
        )
    resumen = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 5,'class':'form-control'})
    )

    director = forms.ModelChoiceField(
        label='Director',
        queryset=Artista.objects.all(),
        widget=forms.Select(attrs={'class':'form-control'}),
        initial='Seleccione una opcion'
    )
    """Se utiliza ModelChoiceField para poder realizar un filtrado de lo que
    quiero mostrar en el selector"""
    genero = forms.ModelChoiceField(
        queryset=Genero.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    portada = forms.ImageField(
         widget=forms.FileInput(attrs={'class':'form-control'})
    )

    Portada_grande = forms.ImageField(
         widget=forms.FileInput(attrs={'class':'form-control'})
    )

    def clean(self):
    # Validar si la pelicula a crear ya existe
     if Pelicula.objects.filter(titulo=self.cleaned_data["titulo"]).exists():
        raise ValidationErr("Ya existe un pelicula con ese titulo")
    
    class Meta:
        model=Pelicula
        fields=['titulo','estreno','portada','resumen','genero','director']  
    


class ArtistasForm(forms.ModelForm):
    # nombre = forms.CharField(error_messages={'required':'Hello! no te olvide de mi!'})

    # def clean_nombre(self):
    #     pass
    
    class Meta:
        model=Artista
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
