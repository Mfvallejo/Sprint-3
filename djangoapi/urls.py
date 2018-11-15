from django.conf.urls import url, include
from .views import CreateUsuarioView
from .views import CreateReservaView
from .views import CreateEspacioView
from .views import CreateParqueaderoView
from .views import CreateOcupadoView

urlpatterns = [
	url('usuarios', CreateUsuarioView.as_view()),
	url('espacios', CreateEspacioView.as_view()),
	url('reservas', CreateReservaView.as_view()),
	url('parqueaderos', CreateParqueaderoView.as_view()),
	url('ocupados', CreateOcupadoView.as_view()),

]


