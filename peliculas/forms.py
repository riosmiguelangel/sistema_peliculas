from django import forms
from django.forms import ValidationError
import re

from administracion.models import User
from django.contrib.auth.forms import UserCreationForm

from django import forms
from django.contrib.auth.models import User
from PIL import Image

def solo_caracteres(value):
     if any(char.isdigit() for char in value):
        raise ValidationError('El nombre no puede contener números. %(valor)s',
                            code='Invalid',
                            params={'valor':value})

def validate_email(value):
        email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if not re.match(email_regex, value):
           raise ValidationError('Correo electrónico inválido')
        return value
 

class ContactoForm(forms.Form):
   
    nombre = forms.CharField(
            label='Nombre', 
            max_length=20,
            validators=(solo_caracteres,),
            error_messages={
                    'required': 'Por favor completa el campo bbbbb'
                },
            widget=forms.TextInput(
                    attrs={'class':'form-control',
                        'placeholder':'Solo letras'}
                    )
        )
    email = forms.EmailField(
            label='Email',
            max_length=100,
            required=False,
            validators=(validate_email,),
            error_messages={
                    'required': 'Por favor completa el campo'
                },
            widget=forms.TextInput(attrs={'class':'form-control','type':'email','placeholder': 'ejemplo@ej.com'})
        )
    
    asunto = forms.CharField(
        label='Asunto',
        max_length=100,
        widget=forms.TextInput(attrs={'class':'form-control'})
    )
    
    mensaje = forms.CharField(
        label='Mensaje',
        min_length=30,
        widget=forms.Textarea(attrs={'rows': 5,'class':'form-control','placeholder': 'Dejanos tu sugerencia'})
    )
   

    def clean_mensaje(self):
        data = self.cleaned_data['mensaje']
        if len(data) < 10:
         raise ValidationError("Debes especificar mejor el mensaje que nos envias")
        return data
    
    
class RegistrarUsuarioForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email' , 'password1', 'password2']

class CalificacionForm(forms.Form):
    puntaje= forms.IntegerField(label="Puntaje", min_value=1)
#     pelicula= forms.IntegerField(label= "pelicula", min_value=1)
#     usuario = forms.IntegerField(label= "usuario", min_value=1)