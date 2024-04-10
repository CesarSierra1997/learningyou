# Generated by Django 4.2.2 on 2024-03-13 10:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Leccion',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('titulo', models.CharField(max_length=200, verbose_name='Titulo de la Lección')),
                ('descripcion', models.CharField(max_length=300, verbose_name='Descripcion')),
                ('fecha_inicio', models.DateField(auto_now=True, verbose_name='fecha de inicio')),
                ('fecha_fin', models.DateField(verbose_name='Fecha de finalización')),
                ('estado', models.BooleanField(default=True, verbose_name='Estado')),
                ('profesor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lecciones', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Leccion',
                'verbose_name_plural': 'Lecciones',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Tarea',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('titulo', models.CharField(max_length=200, verbose_name='Titulo de la Tarea')),
                ('descripcion', models.CharField(max_length=300, verbose_name='Descripcion')),
                ('fecha_inicio', models.DateField(auto_now=True, verbose_name='fecha de inicio')),
                ('fecha_fin', models.DateField(verbose_name='Fecha de finalización')),
                ('estado', models.BooleanField(default=True, verbose_name='Estado')),
                ('leccion_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cohorte.leccion')),
            ],
            options={
                'verbose_name': 'Tarea',
                'verbose_name_plural': 'Tareas',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Evidencia',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('descripcion', models.CharField(max_length=300, verbose_name='Descripcion')),
                ('archivo', models.FileField(upload_to='evidencias/', verbose_name='Archivo')),
                ('fecha_inicio', models.DateField(auto_now=True, verbose_name='fecha de inicio')),
                ('tarea_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cohorte.tarea')),
            ],
            options={
                'verbose_name': 'Evidencia',
                'verbose_name_plural': 'Evidencias',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Cohorte',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('codigo', models.CharField(max_length=200, verbose_name='Codigo Cohorte')),
                ('titulo', models.CharField(max_length=200, verbose_name='Titulo Cohorte')),
                ('fecha_inicio', models.DateField(auto_now=True, verbose_name='fecha de inicio')),
                ('fecha_fin', models.DateField(verbose_name='Fecha de finalización')),
                ('estado', models.BooleanField(default=True, verbose_name='Estado')),
                ('estudiante', models.ManyToManyField(related_name='cohortes_estudiante', to=settings.AUTH_USER_MODEL)),
                ('leccion_id', models.ManyToManyField(related_name='cohortes_leccion', to='cohorte.leccion')),
            ],
            options={
                'verbose_name': 'Cohorte',
                'verbose_name_plural': 'Cohortes',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Calificacion',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('calificacion', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Calificación')),
                ('observacion', models.CharField(max_length=300, verbose_name='Observación')),
                ('fecha_inicio', models.DateField(auto_now=True, verbose_name='fecha de inicio')),
                ('evidencia_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cohorte.evidencia')),
            ],
            options={
                'verbose_name': 'Calificacion',
                'verbose_name_plural': 'Calificaciones',
                'ordering': ['-id'],
            },
        ),
    ]
