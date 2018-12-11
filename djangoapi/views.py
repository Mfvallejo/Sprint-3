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
from django.contrib.auth.decorators import login_required
import json, requests
from django.http import JsonResponse
from django.conf import settings
import os
import logging

dbHost = os.environ['DB_HOST']
dbPort = os.environ['DB_PORT']
mongoDB = os.environ['MONGO_DB']
mlabUser = os.environ['MLAB_USER']
mlabPass = os.environ['MLAB_PASSWORD']

client = MongoClient(dbHost, int(dbPort))
db = client[mongoDB]
db.authenticate(mlabUser, mlabPass)

# Create your views here.

@login_required
def EspaciosList(request):

	queryset = EspacioModel.objects.all()
	context = {
		'espacios_list': queryset
	}
	return render(request, 'Espacios/espacios.html', context)

@login_required
def UsuariosList(request):
	queryset = UsuarioModel.objects.all()
	role = getRole(request)
	context = {
		'usuarios_list': queryset,
		'role': role
	}
	return render(request, 'Usuarios/usuarios.html', context)


def ParqueaderosList(request):
	queryset = ParqueaderoModel.objects.all()
	context = {
		'parqueaderos_list': queryset
	}
	return render(request, 'Parqueaderos/parqueaderos.html', context)

@login_required
def ReservasList(request):
	queryset = ReservaModel.objects.all()
	context = {
		'reservas_list': queryset
	}
	print(context)
	return render(request, 'Reservas/reservas.html', context)

def index(request):
	return render(request, 'index.html')

@login_required
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
	if request.method == "GET":
			data = cole.find({})
			result = []
			for dto in data:
				jsonData ={
					'id': str(dto['id']),
					"reserva": dto['reserva']
				}
				result.append(jsonData)
			return JsonResponse(result, safe=False)

def getRole(request):
	user = request.user
	auth0user = user.social_auth.get(provider="auth0")
	accessToken = auth0user.extra_data['access_token']
	url = "https://isis2503-msaravia98.auth0.com/userinfo"
	headers = {'authorization': 'Bearer ' + accessToken}
	resp = requests.get(url, headers=headers)
	userinfo = resp.json()
	role = userinfo['https://isis2503-msaravia98:auth0:com/role']
	return (role)
