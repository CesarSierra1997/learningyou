from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.generic import TemplateView, ListView, UpdateView,CreateView, DeleteView, View #DetailView
from django.urls import reverse_lazy
from .forms import *
from .models import *


# Vistas basadas en Clases
class Inicio(TemplateView): #vista basada en clases para una sola vista
    def get(self, request, *args, **kwargs):
        return render(request, 'index.html')

#LECCIONES
class ListarLecciones(View):
    model = Leccion
    template_name = 'cohorte/leccion/listar_leccion.html'
    form_class = LeccionForm
    
    # def get_queryset(self):  UTILIZAR PARA V2 DE LA APP
    #     return self.request.user.lecciones.filter(estado=True).order_by('id')

    def get_queryset(self):
        return self.model.objects.filter(estado=True).order_by('id')
    
    def get_context_data(self, **kwargs):
        context = {}
        lecciones = self.get_queryset()
        context["lecciones"] = lecciones
        context["form"] = self.form_class()
        context["cohortes"] = Cohorte.objects.filter(leccion_id__in=lecciones).distinct()
        return context
    
    def get(self, request, *args, **kwargs):
            return render(request, self.template_name, self.get_context_data())
    
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cohorte:listar_leccion')
        else:
            form = self
            return render(request, self.template_name, self.get_context_data())
        
class CrearLeccion(CreateView):
    model = Leccion
    form_class = LeccionForm
    template_name = "cohorte/leccion/crear_leccion.html"
    success_url = reverse_lazy('cohorte:listar_leccion')

class ActualizarLeccion(UpdateView): #Editar en el front
    model = Leccion
    form_class = LeccionForm
    template_name = "cohorte/leccion/leccion.html"  
    success_url = reverse_lazy('cohorte:listar_leccion')

    def get_context_data(self, **kwargs): #para enviar datos con el metodo post
        context = super().get_context_data(**kwargs)
        context['lecciones'] = self.form_class
        return context

class EliminarLeccion(DeleteView):
    model : Leccion
    queryset = Leccion.objects.all()

    def post(self, request, pk, *args, **kwargs):
        object = Leccion.objects.get(id = pk)
        object.estado = False
        object.save()
        return redirect("cohorte:listar_leccion")


#COHORTES
class ListarCohortes(View):
    model = Cohorte
    template_name = 'cohorte/cohorte/listar_cohorte.html'
    form_class = CohorteForm
    
    # def get_queryset(self):
    #     # Filtrar las cohortes asociadas al usuario autenticado
    #     return self.request.user.cohortes_estudiante.filter(estado=True).order_by('id')
    def get_queryset(self):
        return self.model.objects.filter(estado=True).order_by('id')

    def get_context_data(self, **kwargs):
        context = {}
        context["cohortes"] = self.get_queryset() 
        context["form"] = self.form_class() 
        return context
    
    def get(self, request, *args, **kwargs):
            return render(request, self.template_name, self.get_context_data())
    
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cohorte:listar_cohorte')
        else:
            form = self
            return render(request, self.template_name, self.get_context_data())
        
class CrearCohorte(CreateView):
    model = Cohorte
    form_class = CohorteForm
    template_name = "cohorte/cohorte/crear_cohorte.html"
    success_url = reverse_lazy('cohorte:listar_cohorte')

class ActualizarCohorte(UpdateView): #Editar en el front
    model = Cohorte
    form_class = CohorteForm
    template_name = "cohorte/cohorte/cohorte.html"  
    success_url = reverse_lazy('cohorte:listar_cohorte')

    def get_context_data(self, **kwargs): #para enviar datos con el metodo post
        context = super().get_context_data(**kwargs)
        context['cohortes'] = self.form_class
        return context

class EliminarCohorte(DeleteView):
    model : Cohorte
    queryset = Cohorte.objects.all()

    def post(self, request, pk, *args, **kwargs):
        object = Cohorte.objects.get(id = pk)
        object.estado = False
        object.save()
        return redirect("cohorte:listar_cohorte")

#TAREAS
class ListarTareas(View):
    model = Tarea
    template_name = 'cohorte/tarea/listar_tarea.html'
    form_class = TareaForm
    
    def get_queryset(self):
        print("MENSAJE EN EL BACK")
        return self.model.objects.filter(estado=True).order_by('id')
    
    def get_context_data(self, **kwargs):
        context = {}
        context["tareas"] = self.get_queryset() 
        context["form"] = self.form_class() 
        return context
    
    def get(self, request, *args, **kwargs):
            return render(request, self.template_name, self.get_context_data())
    
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cohorte:listar_tarea')
        else:
            form = self
            return render(request, self.template_name, self.get_context_data())
        
class CrearTarea(CreateView):
    model = Tarea
    form_class = TareaForm
    template_name = "cohorte/tarea/crear_tarea.html"
    success_url = reverse_lazy('cohorte:listar_tarea')

class ActualizarTarea(UpdateView): #Editar en el front
    model = Tarea
    form_class = TareaForm
    template_name = "cohorte/tarea/tarea.html"  
    success_url = reverse_lazy('cohorte:listar_tarea')

    def get_context_data(self, **kwargs): #para enviar datos con el metodo post
        context = super().get_context_data(**kwargs)
        context['tareas'] = self.form_class
        return context

class EliminarTarea(DeleteView):
    model : Tarea
    queryset = Tarea.objects.all()

    def post(self, request, pk, *args, **kwargs):
        object = Tarea.objects.get(id = pk)
        object.estado = False
        object.save()
        return redirect("cohorte:listar_tarea")
    
#Evidencias
class ListarEvidencias(View):
    model = Evidencia
    template_name = 'cohorte/evidencia/listar_evidencia.html'
    form_class = EvidenciaForm
    
    def get_queryset(self):
        print("MENSAJE EN EL BACK")
        return self.model.objects.all().order_by('id')
    
    def get_context_data(self, **kwargs):
        context = {}
        context["evidencias"] = self.get_queryset() 
        context["form"] = self.form_class() 
        return context
    
    def get(self, request, *args, **kwargs):
            return render(request, self.template_name, self.get_context_data())
    
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cohorte:listar_evidencia')
        else:
            form = self
            return render(request, self.template_name, self.get_context_data())
        
class CrearEvidencia(CreateView):
    model = Evidencia
    form_class = EvidenciaForm
    template_name = "cohorte/evidencia/crear_evidencia.html"
    success_url = reverse_lazy('cohorte:listar_evidencia')

class ActualizarEvidencia(UpdateView): #Editar en el front
    model = Evidencia
    form_class = EvidenciaForm
    template_name = "cohorte/evidencia/evidencia.html"  
    success_url = reverse_lazy('cohorte:listar_evidencia')

    def get_context_data(self, **kwargs): #para enviar datos con el metodo post
        context = super().get_context_data(**kwargs)
        context['evidencias'] = self.form_class
        return context

class EliminarEvidencia(DeleteView):
    model : Evidencia
    queryset = Evidencia.objects.all()

    def post(self, request, pk, *args, **kwargs):
        object = Evidencia.objects.get(id = pk)
        object.delete()
        return redirect("cohorte:listar_evidencia")
    
#Calificacions
class ListarCalificaciones(View):
    model = Calificacion
    template_name = 'cohorte/calificacion/listar_calificacion.html'
    form_class = CalificacionForm
    
    def get_queryset(self):
        print("MENSAJE EN EL BACK")
        return self.model.objects.all().order_by('id')
    
    def get_context_data(self, **kwargs):
        context = {}
        context["calificaciones"] = self.get_queryset() 
        context["form"] = self.form_class() 
        return context
    
    def get(self, request, *args, **kwargs):
            return render(request, self.template_name, self.get_context_data())
    
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cohorte:listar_calificacion')
        else:
            form = self
            return render(request, self.template_name, self.get_context_data())
        
class CrearCalificacion(CreateView):
    model = Calificacion
    form_class = CalificacionForm
    template_name = "cohorte/calificacion/crear_calificacion.html"
    success_url = reverse_lazy('cohorte:listar_calificacion')

class ActualizarCalificacion(UpdateView): #Editar en el front
    model = Calificacion
    form_class = CalificacionForm
    template_name = "cohorte/calificacion/calificacion.html"  
    success_url = reverse_lazy('cohorte:listar_calificacion')

    def get_context_data(self, **kwargs): #para enviar datos con el metodo post
        context = super().get_context_data(**kwargs)
        context['calificaciones'] = self.form_class
        return context
