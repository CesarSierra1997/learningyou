#importar librerias forms y el modelo Autor
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from django import forms
from .models import *

class LeccionForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(LeccionForm, self).__init__(*args, **kwargs)
        # Filtrar los usuarios por el rol "profesor"
        self.fields['profesor'].queryset = Usuario.objects.filter(rol__rol='profesor')

    class Meta:
        model = Leccion
        fields = ['titulo','descripcion','fecha_fin','profesor']
        labels = { 
            'titulo': 'Titulo de la Lección',
            'descripcion': 'Descripcion',
            'fecha_fin': 'Fecha de finalización',
            'profesor': 'Profesor'
        }
        widgets = {
            'titulo': forms.TextInput(attrs={'class':'form-control','placeholder':'Indique el titulo de la leccion'}),
            'descripcion': forms.Textarea(attrs={'class':'form-control','placeholder':'Indique una breve descripcion de la leccion','style': 'height: 100px;'}),
            'fecha_fin': forms.SelectDateWidget(attrs={'class':'form-control'}),
            'profesor': forms.Select(attrs={'class':'form-control'}),
        }
    
    def clean_titulo(self):
        titulo = self.cleaned_data.get('titulo')
        caracteres_permitidos = set(" 1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
        if not all(char in caracteres_permitidos for char in titulo):
            raise ValidationError(_('Solo se permiten letras y numeros para el titulo de la lección'))
        return titulo.lower()

    def clean_descripcion(self):
        descripcion = self.cleaned_data.get('descripcion')
        caracteres_permitidos = set(" /-*+._,1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
        if not all(char in caracteres_permitidos for char in descripcion):
            raise ValidationError(_('Se permiten solo caracteres alfanuméricos y los siguientes especiales: /, *, -, +, ., _'))
        return descripcion
    
    def clean_fecha_fin(self):
        cleaned_data = self.cleaned_data
        fecha_fin = cleaned_data.get('fecha_fin')
        fecha_actual = timezone.now().date()
        if fecha_fin and fecha_fin <= fecha_actual:
            raise ValidationError("La fecha de finalización debe ser posterior a la fecha actual.")
        return fecha_fin
    


class CohorteForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(CohorteForm, self).__init__(*args, **kwargs)
        # Filtrar los usuarios por el rol "profesor"
        self.fields['estudiante'].queryset = Usuario.objects.filter(rol__rol='estudiante')

    class Meta:
        model = Cohorte
        fields = ['codigo','titulo','fecha_fin','leccion_id','estudiante']
        labels = { 
            'codigo': 'Codigo Cohorte',
            'titulo': 'Titulo Cohorte',
            'fecha_fin': 'Fecha de finalización',
            'leccion_id': 'Leccciones',
            'estudiante': 'Estudiantes'
        }
        widgets = {
            'codigo': forms.TextInput(attrs={'class':'form-control','placeholder':'Indique el codigo de la cohorte' }),
            'titulo': forms.TextInput(attrs={'class':'form-control' ,'placeholder':'Indique el titulo de la cohorte'}),
            'fecha_fin': forms.SelectDateWidget(attrs={'class':'form-control'}),
            'leccion_id': forms.SelectMultiple(attrs={'class':'form-control'}),
            'estudiante': forms.SelectMultiple(attrs={'class':'form-control'}),
        }
    def clean_codigo(self):
        codigo = self.cleaned_data.get('codigo')
        if not codigo.isdigit():
            raise forms.ValidationError("El código solo debe contener números.")
        return codigo

    def clean_titulo(self):
        titulo = self.cleaned_data.get('titulo')
        caracteres_permitidos = set(" 1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
        if not all(char in caracteres_permitidos for char in titulo):
            raise ValidationError(_('Solo se permiten letras y numeros para el titulo de la lección'))
        return titulo.lower()

    def clean_descripcion(self):
        descripcion = self.cleaned_data.get('descripcion')
        caracteres_permitidos = set(" /-*+._,1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
        if not all(char in caracteres_permitidos for char in descripcion):
            raise ValidationError(_('Se permiten solo caracteres alfanuméricos y los siguientes especiales: /, *, -, +, ., _'))
        return descripcion
    
    def clean_fecha_fin(self):
        cleaned_data = self.cleaned_data
        fecha_fin = cleaned_data.get('fecha_fin')
        fecha_actual = timezone.now().date()
        if fecha_fin and fecha_fin <= fecha_actual:
            raise ValidationError("La fecha de finalización debe ser posterior a la fecha actual.")
        return fecha_fin

class TareaForm(forms.ModelForm):
    class Meta:
        model = Tarea
        fields = ['titulo','descripcion','fecha_fin', 'leccion_id']
        labels = { 
            'titulo': 'Titulo de la Tarea',
            'descripcion': 'Descripcion',
            'fecha_fin': 'Fecha de finalización',
            'leccion_id': 'Lección'
        }
        widgets = {
            'titulo': forms.TextInput(attrs={'class':'form-control','placeholder':'Indique el titulo de la tarea'}),
            'descripcion': forms.Textarea(attrs={'class':'form-control','placeholder':'Indique una breve descripcion de la tarea','style': 'height: 100px;'}),
            'fecha_fin': forms.SelectDateWidget(attrs={'class':'form-control'}),
            'leccion_id': forms.Select(attrs={'class':'form-control'}),
        }

    def clean_titulo(self):
        titulo = self.cleaned_data.get('titulo')
        caracteres_permitidos = set(" 1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
        if not all(char in caracteres_permitidos for char in titulo):
            raise ValidationError(_('Solo se permiten letras y numeros para el titulo de la lección'))
        return titulo.lower()

    def clean_descripcion(self):
        descripcion = self.cleaned_data.get('descripcion')
        caracteres_permitidos = set(" /-*+._,1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
        if not all(char in caracteres_permitidos for char in descripcion):
            raise ValidationError(_('Se permiten solo caracteres alfanuméricos y los siguientes especiales: /, *, -, +, ., _'))
        return descripcion
    
    def clean_fecha_fin(self):
        cleaned_data = self.cleaned_data
        fecha_fin = cleaned_data.get('fecha_fin')
        fecha_actual = timezone.now().date()
        if fecha_fin and fecha_fin <= fecha_actual:
            raise ValidationError("La fecha de finalización debe ser posterior a la fecha actual.")
        return fecha_fin

class EvidenciaForm(forms.ModelForm):
    class Meta:
        model = Evidencia
        fields = ['tarea_id','descripcion','archivo']
        labels = { 
            'descripcion': 'Descripcion',
            'archivo': 'Archivo',
            'tarea_id': 'Tarea'
        }
        widgets = {
            'tarea_id': forms.Select(attrs={'class':'form-control'}),
            'descripcion': forms.Textarea(attrs={'class':'form-control','placeholder':'Indique una breve descripcion de la evidencia','style': 'height: 100px;'}),
            'archivo': forms.FileInput(attrs={'class':'form-control'}),
        }

    def clean_descripcion(self):
        descripcion = self.cleaned_data.get('descripcion')
        caracteres_permitidos = set(" /-*+._,1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
        if not all(char in caracteres_permitidos for char in descripcion):
            raise ValidationError(_('Se permiten solo caracteres alfanuméricos y los siguientes especiales: /, *, -, +, ., _'))
        return descripcion

    def clean_archivo(self):
        archivo = self.cleaned_data.get('archivo')
        if archivo:
            extension = archivo.name.split('.')[-1]
            allowed_extensions = ['pdf', 'jpg', 'png', 'docx']
            if extension not in allowed_extensions:
                raise ValidationError('Solo se permiten archivos Pdf, Jpg, Png y Docx.')
        return archivo

class CalificacionForm(forms.ModelForm):
    class Meta:
        model = Calificacion
        fields = ['evidencia_id','observacion' ,'calificacion']
        labels = { 
            'calificacion': 'Agregue una Calificación de 0 a 10',
            'evidencia_id': 'Evidencia',
            'observacion': 'Observación'
        }
        widgets = {
            'calificacion': forms.NumberInput(attrs={'class':'form-control'}),
            'observacion': forms.Textarea(attrs={'class':'form-control','placeholder':'Indique una breve observación de la calificación','style': 'height: 100px;'}),
            'evidencia_id': forms.Select(attrs={'class':'form-control'}),
        }
    
    def clean_calificacion(self):
        calificacion = self.cleaned_data.get('calificacion')
        if not (0 <= calificacion <= 10):
            raise forms.ValidationError("La calificación debe estar entre 0 y 10.")
        return calificacion