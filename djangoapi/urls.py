from django.conf.urls import url, include
from .views import UsuariosList
from .views import CreateReservaView
from .views import EspaciosList
from .views import ParqueaderosList
from .views import CreateOcupadoView

urlpatterns = [
	url('usuarios', UsuariosList),
	url('espacios', EspaciosList),
	url('reservas', CreateReservaView.as_view()),
	url('parqueaderos', ParqueaderosList),
	url('ocupados', CreateOcupadoView.as_view()),

]


