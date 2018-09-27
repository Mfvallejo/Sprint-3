
from django.db import models

# Create your models here.
class UsuarioModel(models.Model):
	n_documento = models.CharField(max_length = 100, blank = False, unique = True, null = False)
	nombre = models.CharField(max_length = 100, blank = False, unique = False, null = False)
	correo = models.CharField(max_length = 150, blank = False, unique = True, null = False)
	edad = models.IntegerField(null = False)
	tipo = models.CharField(max_length = 100, blank = False, unique = False, null = False) # cliente natural -> 'natural', cliente corporativo -> 'juridico'

class OferenteEspacioModel(models.Model):
	id_usuario = models.CharField(max_length = 100, blank = False, unique = False, null = False)
	id_espacio = models.CharField(max_length = 100, blank = False, unique = False, null = False)

class ClienteReservaModel(models.Model):
	id_usuario = models.CharField(max_length = 100, blank = False, unique = False, null = False)
	id_reserva = models.CharField(max_length = 100, blank = False, unique = False, null = False)

class ReservaModel(models.Model):
	id_cliente = models.CharField(max_length = 100, blank = False, unique = False, null = False)
	fecha_inicio = models.CharField(max_length = 100, blank = False, unique = False, null = False)
	fecha_fin = models.CharField(max_length = 100, blank = False, unique = False, null = False)

class EspaResModel (models.Model):
	id_reserva = models.CharField(max_length = 100, blank = False, unique = False, null = False)
	id_espacio = models.CharField(max_length = 100, blank = False, unique = False, null = False)

class EspacioModel(models.Model):
	id_oferente = models.CharField(max_length = 100, blank = False, unique = False, null = False)
	longitud = models.CharField(max_length = 100, blank = False, unique = False, null = False)
	latitud = models.CharField(max_length = 100, blank = False, unique = False, null = False)
	estado = models.IntegerField(blank = False, unique = False, null = False) # 1 para reservado, 0 para disponible
	tipo_vehiculo = models.IntegerField(blank = False,unique = False, null = False)


