from django import forms
from django.core.exceptions import ValidationError
from .models import Formulario
from datetime import date

class FormularioForm(forms.ModelForm):
    class Meta:
        model = Formulario
        fields = '__all__'
        widgets = {
            'fecha_elaboracion': forms.DateInput(attrs={'type': 'date'}),
            'fecha_atencion': forms.DateInput(attrs={'type': 'date'}),
            'fecha_nacimiento': forms.DateInput(attrs={'type': 'date'}),
        }

    def clean_fecha_elaboracion(self):
        fecha = self.cleaned_data['fecha_elaboracion']
        if fecha > date.today():
            raise ValidationError("La fecha de elaboración no puede ser futura")
        return fecha

    def clean_fecha_atencion(self):
        fecha = self.cleaned_data['fecha_atencion']
        if fecha > date.today():
            raise ValidationError("La fecha de atención no puede ser futura")
        return fecha

    def clean_fecha_nacimiento(self):
        fecha = self.cleaned_data['fecha_nacimiento']
        if fecha > date.today():
            raise ValidationError("La fecha de nacimiento no puede ser futura")
        return fecha

    def clean_numero_identificacion(self):
        numero = self.cleaned_data['numero_identificacion']
        if not numero.isdigit():
            raise ValidationError("El número de identificación debe ser numérico")
        return numero

    def clean_telefono(self):
        telefono = self.cleaned_data['telefono']
        if not telefono.isdigit():
            raise ValidationError("El teléfono debe contener solo números")
        return telefono