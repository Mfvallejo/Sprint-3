from django.shortcuts import render
from rest_framework import generics
from rest_framework.renderers import JSONRenderer
import json
import re
from .serializers import UsuarioSerializer
from .serializers import ReservaSerializer
from .serializers import EspacioSerializer
from .models import UsuarioModel
from .models import ReservaModel
from .models import EspacioModel
import json, time
from kafka import KafkaProducer
from kafka.errors import KafkaError
from random import uniform


# Create your views here.
producer = KafkaProducer(bootstrap_servers=['172.24.41.142:8081'],
                                                value_serializer=lambda v: json.dumps(v).encode('utf-8'))


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

"""class CreateEspaResView(generics.ListCreateAPIView):
	This class defines the create behavior of our rest api.
	queryset = EspaResModel.objects.all()
	serializer_class = EspaResSerializer

	def perform_create(self, serializer):
		Save the post data when creating a new bucketlist.
		serializer.save()
		data = JSONRenderer().render(serializer.data)
		new_data_str = str(data).replace('b','')
		values = new_data_str.split(',')
		id_espacio = re.findall('\d+', values[1])[0]
		id_reserva = re.findall('\d+', values[0])[0]
		print('ID espacio: ' + str(id_espacio))
		producer.send('notification-reserved-space', {'id_espacio': id_espacio,
                                        'id_reserva': id_reserva})
		producer.flush()"""
