from django.contrib import admin
from .models import UsuarioModel
from .models import ReservaModel
from .models import EspacioModel

# Register your models here.

admin.site.register(UsuarioModel)
admin.site.register(ReservaModel)
admin.site.register(EspacioModel)


