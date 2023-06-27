
from django.shortcuts import render, redirect,get_object_or_404
from administracion.models import Pelicula

from administracion.models import Elenco
from administracion.models import Plataforma
from administracion.models import Donde_ver_pelicula
from administracion.models import Calificacion
from django.contrib.auth.models import User



from django.views.generic import ListView
from django.contrib import messages

from django.core.mail import send_mail
from django.conf import settings



from peliculas.forms import RegistrarUsuarioForm, ContactoForm
from django.contrib import messages

from django.contrib.auth.views import LogoutView





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
    ver_plataformas = Plataforma.objects.all()
    
    return render(request, 'peliculas/welcome.html', {'peliculas':peliculas, 'artistas':artistas, 'plataformas':plataformas, 'ver_plataformas':ver_plataformas})

def contacto(request):
      if(request.method=='POST'):
        contacto_form = ContactoForm(request.POST)
        if(contacto_form.is_valid()):  
            messages.success(request,'Hemos recibido tus datos')  
            # messages.info(request,'esto es otro tipo')    
            mensaje=f"De: {contacto_form.cleaned_data['nombre']} <{contacto_form.cleaned_data['email']}>\n Asunto: {contacto_form.cleaned_data['asunto']}\n Mensaje: {contacto_form.cleaned_data['mensaje']}"
            mensaje_html=f"""<p>De: {contacto_form.cleaned_data['nombre']} <a href="mailto:{contacto_form.cleaned_data['email']}">{contacto_form.cleaned_data['email']}</a></p>
                <p>Asunto:  {contacto_form.cleaned_data['asunto']}</p>
                <p>Mensaje: {contacto_form.cleaned_data['mensaje']}</p><p>De: {contacto_form.cleaned_data['nombre']} <a href="mailto:{contacto_form.cleaned_data['email']}">{contacto_form.cleaned_data['email']}</a></p>
                <p>Mensaje: {contacto_form.cleaned_data['mensaje']}</p>"""

            asunto="CONSULTA DESDE LA PAGINA - "+contacto_form.cleaned_data['asunto']
            send_mail(
                asunto,
                mensaje,
                settings.EMAIL_HOST_USER,
                [settings.RECIPIENT_ADDRESS],
                fail_silently=False,
                html_message=mensaje_html
            )  
            contacto_form = ContactoForm() #reset formulario
            # acción para tomar los datos del formulario            
        else:
            messages.warning(request,'Por favor revisa los errores en el formulario')
      else:
        contacto_form = ContactoForm()
      context = {                              
                'contacto_form':contacto_form
            }
    
      return render(request,'peliculas/contacto.html',context)

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
    next_page = 'welcome'

    def dispatch(self, request, *args, **kwargs):
        response = super().dispatch(request, *args, **kwargs)
        messages.add_message(request, messages.INFO, 'Se ha cerrado la session correctamente.')
        return response
    
# @login_required
def home_peliculas(request):
    peliculas = Pelicula.objects.all()
    artistas = Elenco.objects.all()
    plataformas = Donde_ver_pelicula.objects.all()
    ver_plataformas = Plataforma.objects.all()
    
    return render(request, 'peliculas/home.html', {'peliculas':peliculas, 'artistas':artistas, 'plataformas':plataformas, 'ver_plataformas':ver_plataformas})

# @login_required
def detalle(request,id_pelicula):
    artistas = Elenco.objects.all()
    plataformas = Donde_ver_pelicula.objects.all()
    calificaciones=Calificacion.objects.all()
    try:
        pelicula = Pelicula.objects.get(pk=id_pelicula)
        verificar_calificacion(request,pelicula)
    except Pelicula.DoesNotExist:
        return render(request,'administracion/404_admin.html')
    return render(request, 'peliculas/detalle.html', {'pelicula':pelicula, 'artistas':artistas, 'plataformas':plataformas, 'calificaciones':calificaciones})



"""
Calificacion estrellas
"""
def verificar_calificacion(request,pelicula):
    artistas = Elenco.objects.all()
    plataformas = Donde_ver_pelicula.objects.all()
    calificaciones=Calificacion.objects.all()
    usuario= request.user
    usuario_id= User.objects.all()
    pelicula_id = Pelicula.objects.all()
    if (pelicula==pelicula_id) and (usuario==usuario_id) :
      if Calificacion.objects.filter(usuario_id==usuario).count():
        info="Ya califico"
      else:
        calificar(request,pelicula)
        return redirect('home')    
    return render(request, 'peliculas/detalle.html', {'pelicula':pelicula, 'artistas':artistas, 'plataformas':plataformas, 'calificaciones':calificaciones}) 


def calificar(request,pelicula):
    usuario= request.user
    # print(usuario)
    if(request.method=='POST'):
        puntos = request.POST["calificacion"]
        # usuario= request.POST["calificacion"]
        calificacion = Calificacion(puntaje= puntos,pelicula=pelicula,usuario=usuario)  
        calificacion.save() 
        return render(request,'peliculas/detalle.html',{'pelicula':pelicula, 'usuario': usuario})
    
    else:
        
        return render(request,'peliculas/home.html')
    



    # if(request.method=='POST'):
    #     formulario = CalificacionForm(request.POST)
    #     if formulario.is_valid():
    #         formulario.save()
    #         return redirect('detalle')