from django.conf.urls import url, include
from .views import UsuariosList
from .views import ReservasList
from .views import CreateReservaView
from .views import EspaciosList
from .views import ParqueaderosList
from .views import CreateOcupadoView

urlpatterns = [
	url('usuarios', UsuariosList),
	url('espacios', EspaciosList),
	url('reservas', ReservasList, name = 'reservas'),
	url('create', CreateReservaView.as_view(), name = 'reservasCreate'),
	url('parqueaderos', ParqueaderosList),
	url('ocupados', CreateOcupadoView.as_view()),

]


