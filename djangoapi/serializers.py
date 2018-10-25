from rest_framework import serializers

from .models import UsuarioModel
from .models import ReservaModel
from .models import EspacioModel

class UsuarioSerializer(serializers.ModelSerializer):
	
	class Meta:
		model = UsuarioModel
		fields = ('n_documento', 'nombre', 'correo', 'edad','tipo')

class EspacioSerializer(serializers.ModelSerializer):
        
        class Meta:
                model = EspacioModel
                fields = ('usuario','longitud','latitud','estado','tipo_vehiculo')

class ReservaSerializer(serializers.ModelSerializer):
	
	espacios= EspacioSerializer(read_only=True, many=True)
	class Meta:
		model = ReservaModel
		fields = ('usuario','fecha_inicio','fecha_fin', 'espacios')


