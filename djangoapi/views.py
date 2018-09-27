from django.shortcuts import render
from rest_framework import generics
from .serializers import UsuarioSerializer
from .serializers import OferenteEspacioSerializer
from .serializers import ClienteReservaSerializer
from .serializers import ReservaSerializer
from .serializers import EspaResSerializer
from .serializers import EspacioSerializer
from .models import UsuarioModel
from .models import OferenteEspacioModel
from .models import ClienteReservaModel
from .models import ReservaModel
from .models import EspaResModel
from .models import EspacioModel


# Create your views here.


class CreateOferenteEspacioView(generics.ListCreateAPIView):
	"""This class defines the create behavior of our rest api."""
	queryset = OferenteEspacioModel.objects.all()
	serializer_class = OferenteEspacioSerializer

	def perform_create(self, serializer):
		"""Save the post data when creating a new bucketlist."""
		serializer.save()

class CreateClienteReservaView(generics.ListCreateAPIView):
        """This class defines the create behavior of our rest api."""
        queryset = ClienteReservaModel.objects.all()
        serializer_class = ClienteReservaSerializer

        def perform_create(self, serializer):
                """Save the post data when creating a new bucketlist."""
                serializer.save()

class CreateUsuarioView(generics.ListCreateAPIView):
        """This class defines the create behavior of our rest api."""
        queryset = UsuarioModel.objects.all()
        serializer_class = UsuarioSerializer

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

class CreateEspacioView(generics.ListCreateAPIView):
        """This class defines the create behavior of our rest api."""
        queryset = EspacioModel.objects.all()
        serializer_class = EspacioSerializer

        def perform_create(self, serializer):
                """Save the post data when creating a new bucketlist."""
                serializer.save()

class CreateEspaResView(generics.ListCreateAPIView):
        """This class defines the create behavior of our rest api."""
        queryset = EspaResModel.objects.all()
        serializer_class = EspaResSerializer

        def perform_create(self, serializer):
                """Save the post data when creating a new bucketlist."""
                serializer.save()

