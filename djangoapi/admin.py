from django.contrib import admin
from .models import OferenteEspacioModel
from .models import ClienteReservaModel
from .models import UsuarioModel
from .models import ReservaModel
from .models import EspacioModel
from .models import EspaResModel
# Register your models here.

admin.site.register(OferenteEspacioModel)
admin.site.register(ClienteReservaModel)
admin.site.register(UsuarioModel)
admin.site.register(ReservaModel)
admin.site.register(EspacioModel)
admin.site.register(EspaResModel)

