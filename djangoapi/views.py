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

class CreateEspacioView(generics.ListCreateAPIView):
        """This class defines the create behavior of our rest api."""
        queryset = EspacioModel.objects.all()
        serializer_class = EspacioSerializer

        def perform_create(self, serializer):
                """Save the post data when creating a new bucketlist."""
                serializer.save()

class CreateOcupadoView(generics.ListCreateAPIView):
        """This class defines the create behavior of our rest api."""
        queryset = OcupadoModel.objects.all()
        serializer_class = OcupadoSerializer

        def perform_create(self, serializer):
                """Save the post data when creating a new bucketlist."""
                serializer.save()

