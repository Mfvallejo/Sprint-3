from django.conf.urls import url, include
from .views import UsuariosList
from .views import ReservasList
from .views import EspaciosList
from .views import ParqueaderosList
from .views import OcupadosList
from .views import index

urlpatterns = [
	url('^$', index),
	url(r'^usuarios', UsuariosList),
	url(r'^espacios', EspaciosList),
	url(r'^reservas', ReservasList),
	url(r'^parqueaderos', ParqueaderosList),
	url(r'^ocupados', OcupadosList),
	url(r'^', include('django.contrib.auth.urls')),
	url(r'^', include('social_django.urls')),
]


