from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.views import generic
from .models import *
from .forms import *
from django.urls import reverse_lazy
from django.contrib import admin
from django.views.generic import TemplateView

# Create your views here.
#shdfoidhlfhw
#lalala
#ek

#reimer me la pela

#wuuuu

class MenuView(TemplateView):
    template_name = 'AppMatriculita/Menu.html'

### Views de Alumnos ###
class Alumnoslistar (generic.ListView):
    template_name = 'Alumnos/index.html'
    model = Alumnos
    context_object_name = "alumnos"

class AlumnosAgregar (generic.CreateView):
    template_name = 'Alumnos/Agregar.html'
    model = Alumnos
    form_class = AlumnosForm
    success_url = reverse_lazy('alumnoslistar')

class AlumnosEditar(generic.UpdateView):
    template_name = 'Alumnos/Editar.html'
    model = Alumnos
    form_class = AlumnosForm
    success_url = reverse_lazy('alumnoslistar')

class AlumnosEliminar(generic.DeleteView):
    template_name = 'Alumnos/Eliminar.html'
    model = Alumnos
    success_url = reverse_lazy('alumnoslistar')


### Views de Carreras ###
class Carreralistar (generic.ListView):
    template_name = 'Carreras/index.html'
    model = Carrera
    context_object_name = "carreras"

class CarreraAgregar (generic.CreateView):
    template_name = 'Carreras/Agregar.html'
    model = Carrera
    form_class = CarreraForm
    success_url = reverse_lazy('carreraslistar')

class CarreraEditar(generic.UpdateView):
    template_name = 'Carreras/Editar.html'
    model = Carrera
    form_class = CarreraForm
    success_url = reverse_lazy('carreraslistar')

class CarreraEliminar(generic.DeleteView):
    template_name = 'Carreras/Eliminar.html'
    model = Carrera
    success_url = reverse_lazy('carreraslistar')




### Views de Clases ###
class Claseslistar (generic.ListView):
    template_name = 'Clases/index.html'
    model = Clases
    context_object_name = "clases"

class ClasesAgregar (generic.CreateView):
    template_name = 'Clases/Agregar.html'
    model = Clases
    form_class = ClasesForm
    success_url = reverse_lazy('carreraslistar')

class ClasesEditar(generic.UpdateView):
    template_name = 'Clases/Editar.html'
    model = Clases
    form_class = ClasesForm
    success_url = reverse_lazy('carreraslistar')

class ClasesEliminar(generic.DeleteView):
    template_name = 'Clases/Eliminar.html'
    model = Clases
    success_url = reverse_lazy('carreraslistar')


### Views de Matricula ###

class Matriculalistar (generic.ListView):
    template_name = 'Matricula/index.html'
    model = Matricula
    context_object_name = "matriculas"

class MatriculaAgregar (generic.CreateView):
    template_name = 'Matricula/Agregar.html'
    model = Matricula
    form_class = MatriculaForm
    success_url = reverse_lazy('matriculaslistar')

class MatriculaEditar(generic.UpdateView):
    template_name = 'Matricula/Editar.html'
    model = Matricula
    form_class = MatriculaForm
    success_url = reverse_lazy('matriculaslistar')

class MatriculaEliminar(generic.DeleteView):
    template_name = 'Matricula/Eliminar.html'
    model = Matricula
    success_url = reverse_lazy('matriculaslistar')


### Asignacion ####

class AsignacionListar (generic.ListView):
    template_name = 'Asignaciones/index.html'
    model = Asignaciones
    context_object_name = "asignaciones"