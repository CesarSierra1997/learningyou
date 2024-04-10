from django.db import models
from ..usuario.models import Usuario

# Create your models here.
class Leccion(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField('Titulo de la Lección',max_length=200, blank=False, null=False)
    descripcion = models.CharField('Descripcion',max_length=300, blank=False, null=False)
    fecha_inicio = models.DateField('fecha de inicio', auto_now=True, auto_now_add=False)
    fecha_fin  = models.DateField('Fecha de finalización', blank=False, null=False)
    estado = models.BooleanField("Estado", default = True)
    profesor = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='lecciones')
    class Meta:
        verbose_name = 'Leccion'
        verbose_name_plural = 'Lecciones'
        ordering = ['-id']

    def __str__(self):
        return ("Leccion: "+self.titulo)

class Cohorte(models.Model):
    id = models.AutoField(primary_key=True)
    codigo = models.CharField('Codigo Cohorte',max_length=200, blank=False, null=False)
    titulo = models.CharField('Titulo Cohorte',max_length=200, blank=False, null=False)
    fecha_inicio = models.DateField('fecha de inicio', auto_now=True, auto_now_add=False)
    fecha_fin  = models.DateField('Fecha de finalización', blank=False, null=False)
    estado = models.BooleanField("Estado", default = True)
    leccion_id = models.ManyToManyField(Leccion, related_name='cohortes_leccion')
    estudiante = models.ManyToManyField(Usuario, related_name='cohortes_estudiante')   

    class Meta:
        verbose_name = 'Cohorte'
        verbose_name_plural = 'Cohortes'
        ordering = ['-id']

    def __str__(self):
        return ("Cohorte: "+self.codigo)

class Tarea(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField('Titulo de la Tarea',max_length=200, blank=False, null=False)
    descripcion = models.CharField('Descripcion',max_length=300, blank=False, null=False)
    fecha_inicio = models.DateField('fecha de inicio', auto_now=True, auto_now_add=False)
    fecha_fin  = models.DateField('Fecha de finalización', blank=False, null=False)
    estado = models.BooleanField("Estado", default = True)
    leccion_id = models.ForeignKey(Leccion, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Tarea'
        verbose_name_plural = 'Tareas'
        ordering = ['-id']

    def __str__(self):
        return ("Tarea: "+self.titulo)

class Evidencia(models.Model):
    id = models.AutoField(primary_key=True)
    descripcion = models.CharField('Descripcion',max_length=300, blank=False, null=False)
    archivo = models.FileField('Archivo', upload_to='evidencias/')
    tarea_id = models.ForeignKey(Tarea, on_delete=models.CASCADE)
    fecha_inicio = models.DateField('fecha de inicio', auto_now=True, auto_now_add=False)

    class Meta:
        verbose_name = 'Evidencia'
        verbose_name_plural = 'Evidencias'
        ordering = ['-id']
    
    def __str__(self):
        return ("Evidencia: "+str(self.id)+" Tarea: "+self.tarea_id.titulo)

class Calificacion(models.Model):
    id = models.AutoField(primary_key=True)
    calificacion = models.DecimalField('Calificación', max_digits=5, decimal_places=2)
    observacion = models.CharField('Observación',max_length=300, blank=False, null=False)
    evidencia_id = models.ForeignKey(Evidencia, on_delete=models.CASCADE)
    fecha_inicio = models.DateField('fecha de inicio', auto_now=True, auto_now_add=False)

    class Meta:
        verbose_name = 'Calificacion'
        verbose_name_plural = 'Calificaciones'
        ordering = ['-id']

    def __str__(self):
        return "Calificación: " + str(self.evidencia_id)
