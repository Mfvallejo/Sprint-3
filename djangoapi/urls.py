from django.conf.urls import url, include
from .views import CreateOferenteEspacioView
from .views import CreateClienteReservaView
from .views import CreateUsuarioView
from .views import CreateReservaView
from .views import CreateEspacioView
from .views import CreateEspaResView

urlpatterns = [
	url('oferentesEspacios', CreateOferenteEspacioView.as_view()),
	url('clientesReservas', CreateClienteReservaView.as_view()),
	url('usuarios', CreateUsuarioView.as_view()),
	url('espaRes', CreateEspaResView.as_view()),
	url('espacios', CreateEspacioView.as_view()),
	url('reservas', CreateReservaView.as_view()),

]


