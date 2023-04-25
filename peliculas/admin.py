from django.contrib import admin

# Register your models here.
from .models import Peliculas
from .models import Generos
from .models import Artistas
from .models import FailedJobs
from .models import Migrations
from .models import PasswordResets
from .models import Users

admin.site.register(Peliculas)
admin.site.register(Generos)
admin.site.register(Artistas)
admin.site.register(FailedJobs)
admin.site.register(Migrations)
admin.site.register(PasswordResets)
admin.site.register(Users)