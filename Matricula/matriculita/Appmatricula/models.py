from django.db import models

# Create your models here.

class Carrera (models.Model):
    Carrera_id = models.CharField(primary_key = True, max_length = 50)
    C_Nombre = models.CharField(max_length = 100)

    def __str__(self):
        return f"{self.Carrera_id} - {self.C_Nombre}"

class Alumnos (models.Model):
    AlumnoID = models.CharField(primary_key = True, max_length = 10)
    Nombre = models.CharField(max_length=100)
    Apellido = models.CharField(max_length=100)
    Identidad = models.CharField(max_length=13)
    Correo = models.EmailField()
    Telefono = models.CharField(max_length=8)
    Direccion = models.CharField(max_length=100)
    sexos = [
        ('F', 'Femenino'),
        ('M', 'Masculino')
    ]
    sexo = models.CharField(max_length=1, choices=sexos, default='F')
    Usuario =  models.CharField(max_length=100)
    Password = models.CharField(max_length=50)
    Carrera_id = models.ForeignKey(Carrera, null = True, blank = False, on_delete=models.PROTECT)

    def __str__(self):
        return f'Alumno #{self.AlumnoID} - {self.Nombre} - Carrera: {self.Carrera_id.C_Nombre}'  

    def clase_predecesora_pasada(self, clase_id):
        clase_predecesora = Clases.objects.get(ClaseID=clase_id).clase_predecesora
        if clase_predecesora:
            clase_predecesora_id = clase_predecesora.ClaseID
            if self.historialalumno_set.filter(ClaseID=clase_predecesora_id, aprobado=True).exists():
                return True
        return False

class Maestros (models.Model):
    MaestroId = models.CharField(primary_key = True, max_length = 10)    
    Nombre = models.CharField(max_length=100)
    Apellido = models.CharField(max_length=100)
    Identidad = models.CharField(max_length=13)
    sexos = [
        ('F', 'Femenino'),
        ('M', 'Masculino')
    ]
    sexo = models.CharField(max_length=1, choices=sexos, default='F')
    Correo = models.EmailField()
    Telefono = models.CharField(max_length=8)
    Direccion = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.MaestroId} - {self.Nombre}" 

class Periodo (models.Model):
    periodo_id = models.BigAutoField(primary_key=True)
    Descripcion = models.CharField(max_length=100)
    Inicio = models.DateField()
    Fin =models.DateField()

    def __str__(self):
        return f"{self.periodo_id} - {self.Descripcion}" 

class Clases(models.Model):
    ClaseID = models.CharField(primary_key=True, max_length=20)
    Nombre = models.CharField(max_length=100)
    clase_predecesora = models.ForeignKey('self', null=True, blank=True, on_delete=models.PROTECT, related_name='clases_siguientes')

    def __str__(self):
        return f"{self.ClaseID} - {self.Nombre}"


class Asignaciones (models.Model):
    Asignacio_Id = models.BigAutoField(primary_key=True)
    periodo_id = models.ForeignKey(Periodo, null=True, blank=False, on_delete=models.PROTECT)
    año = models.IntegerField()
    MaestroId = models.ForeignKey(Maestros, null=True, blank=False, on_delete=models.PROTECT)
    ClaseID = models.ForeignKey(Clases, null=True, blank=False, on_delete=models.PROTECT)
    hora_inicio = models.TimeField(default="00:00:00")
    hora_fin = models.TimeField(default="00:00:00")

    def __str__(self):
        return f'Asignaciones #{self.Asignacio_Id} - {self.año} - Periodo:{self.periodo_id.Descripcion} - Maestros:{self.MaestroId.Nombre} - Clases:{self.ClaseID.Nombre}'




class HistorialAlumno (models.Model):
    HistoId = models.BigAutoField(primary_key=True)
    AlumnoID = models.ForeignKey(Alumnos, null = True, blank = False, on_delete=models.PROTECT)
    ClaseID = models.ForeignKey(Clases, null = True, blank = False, on_delete=models.PROTECT)
    periodo_id = models.ForeignKey(Periodo, null = True, blank = False, on_delete=models.PROTECT)
    MaestroId = models.ForeignKey(Maestros, null = True, blank = False, on_delete=models.PROTECT)
    aprobado = models.BooleanField(default=False)

    def __str__(self):
        return f'HistorialAlumno #{self.HistoId} - Alumnos:{self.AlumnoID.Nombre} - Clases:{self.ClaseID.Nombre} - Periodo : {self.periodo_id.Descripcion} - MaestroId: {self.MaestroId.Nombre}'



class Matricula(models.Model):
    Matricula_id = models.BigAutoField(primary_key=True)
    alumno = models.ForeignKey(Alumnos, null=True, blank=False, on_delete=models.PROTECT)
    asignacion = models.ForeignKey(Asignaciones, null=True, blank=False, on_delete=models.PROTECT)
    aprobado = models.BooleanField(default=False)

    def __str__(self):
        if self.asignacion is not None:
            return f'Matricula #{self.Matricula_id} - {self.alumno.Nombre} - {self.asignacion.año} - {self.asignacion.periodo_id.Descripcion} - {self.asignacion.MaestroId.Nombre} - {self.asignacion.ClaseID.Nombre}'
        else:
            return f'Matricula #{self.Matricula_id} - {self.alumno.Nombre} - Asignación: None - Aprobado: {self.aprobado}'


class Factura(models.Model):
    Fact_id = models.BigAutoField(primary_key=True)
    alumno = models.ForeignKey(Alumnos, null=True, blank=False, on_delete=models.PROTECT)
    matricula = models.ForeignKey(Matricula, null=True, blank=False, on_delete=models.PROTECT)
    total = models.FloatField(default=0)

    def __str__(self):
        return f'Factura #{self.Fact_id} - {self.alumno.Nombre} - Total: {self.total}'


class Clase(models.Model):
    C_ID = models.BigAutoField(primary_key=True)
    clase = models.ForeignKey(Clases, null=True, blank=False, on_delete=models.PROTECT)
    matri = models.ForeignKey(Matricula, null=True, blank=False, on_delete=models.PROTECT)
    precio = models.FloatField(default=800)

    def __str__(self):
        return f'Clase #{self.C_ID} - {self.clase.Nombre} - Precio: {self.precio}' 

