from django.urls import path,re_path,include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    # path('peliculas_index', views.peliculas_index, name="peliculas_index"),
    # path('', views.home_show, name="welcome"),
    path('', views.home_peliculas, name="home"),
   
    path('peliculas/detalle/<int:id_pelicula>', views.detalle,name='detalle'),

   
    # path('detalle_pelicula/<int:id_pelicula>', views.detalle_pelicula, name="detalle_pelicula"),
    

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
]

