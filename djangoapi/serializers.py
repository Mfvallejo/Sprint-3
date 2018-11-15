from rest_framework import serializers
from .models import UsuarioModel
from .models import ParqueaderoModel
from .models import EspacioModel
from .models import ReservaModel
from .models import OcupadoModel

class UsuarioSerializer(serializers.ModelSerializer):
		
	class Meta:
		model = UsuarioModel
		fields = ('n_documento', 'nombre', 'correo', 'edad','tipo')

class ParqueaderoSerializer(serializers.ModelSerializer):
		
	class Meta:
		model = ParqueaderoModel
		fields = ('usuario', 'direccion', 'longitud','latitud')

class EspacioSerializer(serializers.ModelSerializer):
		
	class Meta:
		model = EspacioModel
		fields = ('parqueadero','estado','tipo_vehiculo','numero')

class ReservaSerializer(serializers.ModelSerializer):

	class Meta:
		model = ReservaModel
		fields = ('usuario','fecha_inicio','fecha_fin', 'ocupados')
		
class OcupadoSerializer(serializers.ModelSerializer):

	class Meta:
		model = OcupadoModel
		fields = ('espacio','reserva','nombre')
