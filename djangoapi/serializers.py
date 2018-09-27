from rest_framework import serializers


from .models import UsuarioModel
from .models import OferenteEspacioModel
from .models import ClienteReservaModel 
from .models import EspaResModel 
from .models import ReservaModel 
from .models import EspacioModel 

class UsuarioSerializer(serializers.ModelSerializer):
	
	class Meta:
		model = UsuarioModel
		fields = ('n_documento', 'nombre', 'correo', 'edad','tipo')

class OferenteEspacioSerializer(serializers.ModelSerializer):
	
	class Meta:
		model = OferenteEspacioModel
		fields = ('id_usuario', 'id_espacio')

class ClienteReservaSerializer(serializers.ModelSerializer):
        
	class Meta:
		model = ClienteReservaModel
		fields = ('id_usuario','id_reserva')

class ReservaSerializer(serializers.ModelSerializer):
        
        class Meta:
                model = ReservaModel
                fields = ('id_cliente','fecha_inicio','fecha_fin')

class EspaResSerializer(serializers.ModelSerializer):
        
        class Meta:
                model = EspaResModel
                fields = ('id_reserva','id_espacio')
class EspacioSerializer(serializers.ModelSerializer):

        class Meta:
                model = EspacioModel
                fields = ('id_oferente','longitud','latitud','estado','tipo_vehiculo')

