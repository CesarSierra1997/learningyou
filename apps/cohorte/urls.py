#Importarmos libreria para las urls
from django.urls import path
from .views import *
from django.contrib.auth.decorators import login_required
urlpatterns = [
    #Lecciones
    path('listar_leccion/', login_required(ListarLecciones.as_view()), name='listar_leccion' ),
    path('crear_leccion/', login_required(CrearLeccion.as_view()), name='crear_leccion' ),
    path('editar_leccion/<int:pk>/', login_required(ActualizarLeccion.as_view()), name='editar_leccion'),   
    path('eliminar_leccion/<int:pk>/', login_required(EliminarLeccion.as_view()), name='eliminar_leccion' ),

    #Cohortes
    path('listar_cohorte/', login_required(ListarCohortes.as_view()), name='listar_cohorte' ),
    path('crear_cohorte/', login_required(CrearCohorte.as_view()), name='crear_cohorte' ),
    path('editar_cohorte/<int:pk>/', login_required(ActualizarCohorte.as_view()), name='editar_cohorte'),   
    path('eliminar_cohorte/<int:pk>/', login_required(EliminarCohorte.as_view()), name='eliminar_cohorte' ),

    #Tareas
    path('listar_tarea/', login_required(ListarTareas.as_view()), name='listar_tarea' ),
    path('crear_tarea/', login_required(CrearTarea.as_view()), name='crear_tarea' ),
    path('editar_tarea/<int:pk>/', login_required(ActualizarTarea.as_view()), name='editar_tarea'),   
    path('eliminar_tarea/<int:pk>/', login_required(EliminarTarea.as_view()), name='eliminar_tarea' ),

    #Evidencias
    path('listar_evidencia/', login_required(ListarEvidencias.as_view()), name='listar_evidencia' ),
    path('crear_evidencia/', login_required(CrearEvidencia.as_view()), name='crear_evidencia' ),
    path('editar_evidencia/<int:pk>/', login_required(ActualizarEvidencia.as_view()), name='editar_evidencia'),   
    path('eliminar_evidencia/<int:pk>/', login_required(EliminarEvidencia.as_view()), name='eliminar_evidencia' ),

    #Calificaciones
    path('listar_calificacion/', login_required(ListarCalificaciones.as_view()), name='listar_calificacion' ),
    path('crear_calificacion/', login_required(CrearCalificacion.as_view()), name='crear_calificacion' ),
    path('editar_calificacion/<int:pk>/', login_required(ActualizarCalificacion.as_view()), name='editar_calificacion'),

]  