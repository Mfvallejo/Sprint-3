from django.db import models

# Create your models here.
class UsuarioModel(models.Model):
	n_documento = models.CharField(max_length = 100, blank = False, unique = True, null = False)
	nombre = models.CharField(max_length = 100, blank = False, unique = False, null = False)
	correo = models.CharField(max_length = 150, blank = False, unique = True, null = False)
	edad = models.IntegerField(null = False)
	tipo = models.CharField(max_length = 100, blank = False, unique = False, null = False) # cliente natural -> 'natural', cliente juridico ->'juridica'

def user_def():
	return UsuarioModel.objects.get(id=1)

class ParqueaderoModel(models.Model):
	usuario  = models.ForeignKey(UsuarioModel, on_delete=models.CASCADE, default= user_def().id)
	direccion = models.CharField(max_length = 100, blank = False, unique = False, null = False)
	longitud = models.CharField(max_length = 100, blank = False, unique = False, null = False)
	latitud = models.CharField(max_length = 100, blank = False, unique = False, null = False)
	nombre = models.CharField(max_length = 100, blank = False, unique = False, null = False)

def  parq_def():
	return ParqueaderoModel.objects.get(id=1)

class EspacioModel(models.Model):
	parqueadero = models.ForeignKey(ParqueaderoModel, on_delete=models.CASCADE, default= parq_def().id)
	estado = models.IntegerField(blank = False, unique = False, null = False) # 1 para reservado, 0 para disponible
	tipo_vehiculo = models.IntegerField(blank = False,unique = False, null = False)
	numero = models.IntegerField(blank = False,unique = False,null = False)

class ReservaModel(models.Model):
	usuario  = models.ForeignKey(UsuarioModel, on_delete=models.CASCADE, default= user_def().id)
	fecha_inicio = models.CharField(max_length = 100, blank = False, unique = False, null = False)
	fecha_fin = models.CharField(max_length = 100, blank = False, unique = False, null = False)
	ocupados = models.ManyToManyField(EspacioModel, through='OcupadoModel')

class OcupadoModel(models.Model):
	espacio = models.ForeignKey(EspacioModel, on_delete=models.CASCADE)
	reserva = models.ForeignKey(ReservaModel, on_delete=models.CASCADE)
	nombre = models.CharField(max_length=100)
