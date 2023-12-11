from django import forms
from .models import *


class CarreraForm (forms.ModelForm):
    class Meta:
        model = Carrera
        fields = '__all__' 


class AlumnosForm (forms.ModelForm):
    class Meta:
        model = Alumnos
        fields = '__all__' 


class MaestrosForm (forms.ModelForm):
    class Meta:
        model = Maestros
        fields = '__all__' 


class PeriodoForm (forms.ModelForm):
    class Meta:
        model = Periodo
        fields = '__all__' 


class ClasesForm (forms.ModelForm):
    class Meta:
        model = Clases
        fields = '__all__' 

class AsignacionForm (forms.ModelForm):
    class Meta:
        model = Asignaciones
        fields = '__all__' 


class HistorialAlumnoForm (forms.ModelForm):
    class Meta:
        model = HistorialAlumno
        fields = '__all__'


class MatriculaForm (forms.ModelForm):
    class Meta:
        model = Matricula
        fields = '__all__' 


class FacturaForm (forms.ModelForm):
    class Meta:
        model = Factura
        fields = '__all__' 
     
class ClaseForm(forms.ModelForm):
    class Meta:
        model = Factura
        fields = '__all__'

class CarreraForm(forms.ModelForm):
    class Meta:
        model = Carrera
        fields = '__all__'