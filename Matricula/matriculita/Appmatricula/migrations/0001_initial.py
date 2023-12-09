# Generated by Django 4.2.8 on 2023-12-08 23:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alumnos',
            fields=[
                ('AlumnoID', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('Nombre', models.CharField(max_length=100)),
                ('Apellido', models.CharField(max_length=100)),
                ('Identidad', models.CharField(max_length=13)),
                ('Correo', models.EmailField(max_length=254)),
                ('Telefono', models.CharField(max_length=8)),
                ('Direccion', models.CharField(max_length=100)),
                ('sexo', models.CharField(choices=[('F', 'Femenino'), ('M', 'Masculino')], default='F', max_length=1)),
                ('Usuario', models.CharField(max_length=100)),
                ('Password', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Asignaciones',
            fields=[
                ('Asignacio_Id', models.BigAutoField(primary_key=True, serialize=False)),
                ('año', models.IntegerField()),
                ('hora_inicio', models.TimeField(default='00:00:00')),
                ('hora_fin', models.TimeField(default='00:00:00')),
            ],
        ),
        migrations.CreateModel(
            name='Carrera',
            fields=[
                ('Carrera_id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('C_Nombre', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Clases',
            fields=[
                ('ClaseID', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('Nombre', models.CharField(max_length=100)),
                ('clase_predecesora', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='clases_siguientes', to='Appmatricula.clases')),
            ],
        ),
        migrations.CreateModel(
            name='Maestros',
            fields=[
                ('MaestroId', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('Nombre', models.CharField(max_length=100)),
                ('Apellido', models.CharField(max_length=100)),
                ('Identidad', models.CharField(max_length=13)),
                ('sexo', models.CharField(choices=[('F', 'Femenino'), ('M', 'Masculino')], default='F', max_length=1)),
                ('Correo', models.EmailField(max_length=254)),
                ('Telefono', models.CharField(max_length=8)),
                ('Direccion', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Periodo',
            fields=[
                ('periodo_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('Descripcion', models.CharField(max_length=100)),
                ('Inicio', models.DateField()),
                ('Fin', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Matricula',
            fields=[
                ('Matricula_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('aprobado', models.BooleanField(default=False)),
                ('alumno', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='Appmatricula.alumnos')),
                ('asignacion', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='Appmatricula.asignaciones')),
            ],
        ),
        migrations.CreateModel(
            name='HistorialAlumno',
            fields=[
                ('HistoId', models.BigAutoField(primary_key=True, serialize=False)),
                ('aprobado', models.BooleanField(default=False)),
                ('AlumnoID', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='Appmatricula.alumnos')),
                ('ClaseID', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='Appmatricula.clases')),
                ('MaestroId', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='Appmatricula.maestros')),
                ('periodo_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='Appmatricula.periodo')),
            ],
        ),
        migrations.CreateModel(
            name='Factura',
            fields=[
                ('Fact_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('total', models.FloatField(default=0)),
                ('alumno', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='Appmatricula.alumnos')),
                ('matricula', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='Appmatricula.matricula')),
            ],
        ),
        migrations.CreateModel(
            name='Clase',
            fields=[
                ('C_ID', models.BigAutoField(primary_key=True, serialize=False)),
                ('precio', models.FloatField(default=800)),
                ('clase', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='Appmatricula.clases')),
                ('matri', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='Appmatricula.matricula')),
            ],
        ),
        migrations.AddField(
            model_name='asignaciones',
            name='ClaseID',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='Appmatricula.clases'),
        ),
        migrations.AddField(
            model_name='asignaciones',
            name='MaestroId',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='Appmatricula.maestros'),
        ),
        migrations.AddField(
            model_name='asignaciones',
            name='periodo_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='Appmatricula.periodo'),
        ),
        migrations.AddField(
            model_name='alumnos',
            name='Carrera_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='Appmatricula.carrera'),
        ),
    ]
