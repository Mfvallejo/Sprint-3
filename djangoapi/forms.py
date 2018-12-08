from django import forms
from .models import ReservaModel

class ReservaForm(forms.ModelForm):
	class Meta:
		model = ReservaModel
		fields = [
			'fecha_fin',
			'ocupados',
		]
		labels = {
			'fecha_fin': 'Fecha Fin',
			'ocupados': 'Ocupados',
		}
		widgets = {
			'fecha_fin': forms.DateField(widget=AdimnDateWidget)
			'ocupados': forms.ModelMultipleChoiceField(queryset = OcupadosModel.objects.all())
