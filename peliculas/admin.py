from django.contrib import admin

# Register your models here.
from .models import Peliculas
from .models import Generos

admin.site.register(Peliculas)
admin.site.register(Generos)