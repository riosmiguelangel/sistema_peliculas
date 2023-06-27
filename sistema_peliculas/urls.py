"""sistema_peliculas URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from administracion  import views
from peliculas  import views
from django.urls.conf import include
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views


from django.conf.urls.static import static
from django.conf import settings
from administracion.admin import sitio_admin

urlpatterns = [
    # path('adminoriginal/', admin.site.urls),
    path('admin/', sitio_admin.urls),
    path('peliculas/',include('peliculas.urls')),
    path('administracion/',include('administracion.urls')),
     #autenticacion
    path('registrarse', views.pelicula_registrarse, name='registrarse'),
    # path('cuentas/login', views.cac_login, name='login'),
    # path('cuentas/logout/',
    #      auth_views.LogoutView.as_view(template_name='cac/publica/index.html'), name='logout'),
    
    #por defecto de django    
    path('accounts/login/', auth_views.LoginView.as_view(
            template_name='peliculas/login.html',
            extra_context={'variable':'TEST'},
        )),
    path('accounts/logout/',
          views.peliculas_LogoutView.as_view(),name='logout'),
    path('accounts/password_change/', auth_views.PasswordChangeView.as_view(success_url="/"), name='password_change'), 
    path('accounts/', include('django.contrib.auth.urls')),
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

