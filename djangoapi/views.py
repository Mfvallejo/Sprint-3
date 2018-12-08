from django.shortcuts import render
from rest_framework import generics
from .serializers import UsuarioSerializer
from .serializers import ParqueaderoSerializer
from .serializers import EspacioSerializer
from .serializers import ReservaSerializer
from .serializers import OcupadoSerializer
from .models import UsuarioModel
from .models import ReservaModel
from .models import EspacioModel
from .models import ParqueaderoModel
from .models import OcupadoModel
import json, requests


# Create your views here.

def EspaciosList(request):

	queryset = EspacioModel.objects.all()
	context = {
		'espacios_list': queryset
	}
	return render(request, 'Espacios/espacios.html', context)

def UsuariosList(request):
	queryset = UsuarioModel.objects.all()
	context = {
		'usuarios_list': queryset
	}
	return render(request, 'Usuarios/usuarios.html', context)

def ParqueaderosList(request):
	queryset = ParqueaderoModel.objects.all()
	context = {
		'parqueaderos_list': queryset
	}
	return render(request, 'Parqueaderos/parqueaderos.html', context)

def ReservasList(request):
	queryset = ReservaModel.objects.all()
	context = {
		'reservas_list': queryset
	}
	print(context)
	return render(request, 'Reservas/reservas.html', context)

def index(request):
	return render(request, 'index.html')

def OcupadosList(request):
	queryset = OcupadoModel.objects.all()
	context = {
		'ocupados_list': queryset
	}
	return render(request, 'Ocupados/ocupados.html', context)

def ReservaCreate(request):
	varName = Variable.objects.get(id=id_usuario)
	form = ReservaForm(request.POST, instance = usuario)
	if form.is_valid():
		form.save()
	return redirect('reservasList')
	return render(request, 'Reserva/reservaCreate.html',{'form':form, 'variable': varName.name})

#def getId(request):

def getRole(request):
	user = request.user
	auth0user = user.social_auth.get(provider="auth0")
	accessToken = auth0user.extra_data['access_token']
	url = "https://isis2503-msaravia98.auth0.com/userinfo"
	headers = {'authorization': 'Bearer ' + accessToken}
	resp = requests.get(url, headers=headers)
	userinfo = resp.json()
	role = userinfo['https://isis2503-msaravia98.auth0:com/role']
	return (role)
