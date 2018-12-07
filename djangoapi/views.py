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

class CreateUsuarioView(generics.ListCreateAPIView):
        """This class defines the create behavior of our rest api."""
        queryset = UsuarioModel.objects.all()
        serializer_class = UsuarioSerializer

        def perform_create(self, serializer):
                """Save the post data when creating a new bucketlist."""
                serializer.save()

class CreateParqueaderoView(generics.ListCreateAPIView):
        """This class defines the create behavior of our rest api."""
        queryset = ParqueaderoModel.objects.all()
        serializer_class = ParqueaderoSerializer

        def perform_create(self, serializer):
                """Save the post data when creating a new bucketlist."""
                serializer.save()

class CreateReservaView(generics.ListCreateAPIView):
        """This class defines the create behavior of our rest api."""
        queryset = ReservaModel.objects.all()
        serializer_class = ReservaSerializer

        def perform_create(self, serializer):
                """Save the post data when creating a new bucketlist."""
                serializer.save()

def EspaciosList(request):

	queryset = EspacioModel.objects.all()
	context = {
		'espacios_list': queryset
	}
	return render(request, 'Espacios/espacios.html', context)

class CreateOcupadoView(generics.ListCreateAPIView):
        """This class defines the create behavior of our rest api."""
        queryset = OcupadoModel.objects.all()
        serializer_class = OcupadoSerializer

        def perform_create(self, serializer):
                """Save the post data when creating a new bucketlist."""
                serializer.save()


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
	return render(request, 'Reservas/reservas.html', context)
