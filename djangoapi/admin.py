from django.contrib import admin
from .models import UsuarioModel
from .models import ReservaModel
from .models import EspacioModel
from .models import ParqueaderoModel
from .models import OcupadoModel

# Register your models here.

admin.site.register(UsuarioModel)
admin.site.register(ReservaModel)
admin.site.register(EspacioModel)
admin.site.register(ParqueaderoModel)
admin.site.register(OcupadoModel)


