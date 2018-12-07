from django.conf.urls import url, include
from .views import UsuariosList
from .views import ReservasList
from .views import CreateReservaView
from .views import EspaciosList
from .views import ParqueaderosList
from .views import CreateOcupadoView
from .views import OcupadosList
from .views import index

urlpatterns = [
	url('^$', index),
	url('usuarios', UsuariosList),
	url('espacios', EspaciosList),
	url('reservas', ReservasList),
	url('parqueaderos', ParqueaderosList),
	url('ocupados', OcupadosList),

]


