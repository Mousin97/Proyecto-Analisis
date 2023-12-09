from django.urls import path
from . import views
from .views import *



urlpatterns = [

path('menu/', MenuView.as_view(), name='menusito'),

    ## --------- URLS DE ALUMNOS --------##
  
path('alumnos', Alumnoslistar.as_view(), name = 'alumnoslistar'),
path('alumnos/agregar', AlumnosAgregar.as_view(), name = 'alumnosagregar'),
path('alumnos/editar/<str:pk>/', AlumnosEditar.as_view(), name = 'alumnoseditar'),
path('alumnos/eliminar/<str:pk>/', AlumnosEliminar.as_view(), name = 'alumnoseliminar'),


    ## --------- URLS DE CARRERAS --------##
  
path('carreras', Carreralistar.as_view(), name = 'carreraslistar'),
path('carreras/agregar', CarreraAgregar.as_view(), name = 'carrerasagregar'),
path('carreras/editar/<str:pk>/', CarreraEditar.as_view(), name = 'carreraseditar'),
path('carreras/eliminar/<str:pk>/', CarreraEliminar.as_view(), name = 'carreraseliminar'),


    ## --------- URLS DE CLASES --------##
  
path('clases', Claseslistar.as_view(), name = 'claseslistar'),
path('clases/agregar', ClasesAgregar.as_view(), name = 'clasesagregar'),
path('clases/editar/<str:pk>/', ClasesEditar.as_view(), name = 'claseseditar'),
path('clases/eliminar/<str:pk>/', ClasesEliminar.as_view(), name = 'claseseliminar'),


    ## --------- URLS DE MATRICULA --------##


path('matriculas', Matriculalistar.as_view(), name = 'matriculaslistar'),
path('matriculas/agregar', MatriculaAgregar.as_view(), name = 'matriculasagregar'),
path('matriculas/editar/<int:pk>/', MatriculaEditar.as_view(), name = 'matriculaseditar'),
path('matriculas/eliminar/int<str:pk>/', MatriculaEliminar.as_view(), name = 'matriculaseliminar'),

    ### -------- URLS DE ASIGNACION -------###

path('asignaciones', AsignacionListar.as_view(), name = 'asignacionlistar')


]
