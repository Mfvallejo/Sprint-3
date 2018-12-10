from pymongo import MongoClient
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
from django.http import JsonResponse
from django.conf import settings

client = MongoClient(settings.DB_HOST, int(settings.DB_PORT))
db = client[settings.MONGO_DB]
db.authenticate(settings.MLAB_USER, settings.MLAB_PASSWORD)

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

def crearReserva(request):
	cole = db['reservas']
	if request.method == 'POST':
		data = JSONParser.parse(request)
		result = cole.insert(data)
		respo ={
	            "MongoObjectID": str(result),
        	    "Message": "Nuevo objeto en la base de datos"
	        }
	return JsonResponse(respo, safe=False)

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
