from xml.dom import ValidationErr
from django import forms
from administracion.models import Genero, Artista,Pelicula,Calificacion
from django.contrib.auth.models import User
from PIL import Image


#-- Calificacion estrellas --
# class CalificacionForm(forms.ModelForm):
#     puntaje = forms.IntegerField(error_messages={'required':'Hello! no te olvide de mi!'})
#     # usuario = forms.ModelChoiceField(queryset=User.objects.all())
#     class Meta:
#         model=Calificacion
#         fields=['puntaje','pelicula','usuario']

        # widgets = {
        #     'puntaje' : forms.TextInput(attrs={'class':'form-control','placeholder':'Ingrese la calificacion'})
        # }
        # error_messages = {
        #     'puntaje' :{
        #         'required':'No te olvides de mi!'
        #     }
        # }

class CalificacionForm(forms.Form):
    puntaje= forms.IntegerField(label="Puntaje", min_value=1)
#     pelicula= forms.IntegerField(label= "pelicula", min_value=1)
#     usuario = forms.IntegerField(label= "usuario", min_value=1)