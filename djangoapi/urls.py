from django.conf.urls import url, include
from .views import CreateUsuarioView
from .views import CreateReservaView
from .views import CreateEspacioView

urlpatterns = [
	url('usuarios', CreateUsuarioView.as_view()),
	url('espacios', CreateEspacioView.as_view()),
	url('reservas', CreateReservaView.as_view()),

]


