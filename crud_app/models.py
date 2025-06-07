from django.db import models
from django.utils import timezone

class Formulario(models.Model):
    REGIMEN_CHOICES = [
        ('SUBSIDIADO', 'Subsidiado'),
        ('CONTRIBUTIVO', 'Contributivo'),
        ('ESPECIAL', 'Especial o de Excepción'),
        ('NO_ASEGURADO', 'No Asegurado'),
    ]
    
    SEXO_CHOICES = [
        ('M', 'Masculino'),
        ('F', 'Femenino'),
    ]
    
    ETNIA_CHOICES = [
        ('1', 'Indígena'),
        ('2', 'ROM'),
        ('3', 'Raizal'),
        ('4', 'Palenquero'),
        ('5', 'Afrodescendiente'),
        ('6', 'Otras etnias'),
        ('Z', 'Sin identificar'),
    ]
    
    GRUPO_POBLACIONAL_CHOICES = [
        ('Indigentes', 'Indigentes'),
        ('Población infantil vulnerable', 'Población infantil vulnerable bajo protección en instituciones diferentes a ICBF'),
        ('Personas en protección a testigos', 'Personas en protección a testigos'),
        ('Población en centros psiquiátricos', 'Población en centros psiquiátricos'),
        ('Población rural migratoria', 'Población rural migratoria'),
        ('Población en centros carcelarios', 'Población en centros carcelarios'),
        ('Población rural no migratoria', 'Población rural no migratoria'),
        ('Adultos mayores en centros de protección', 'Adultos mayores en centros de protección'),
        ('Comunidades indígenas', 'Comunidades indígenas'),
        ('Población ROM', 'Población ROM'),
        ('Afrocolombianos', 'Afrocolombianos'),
        ('Población infantil ICBF', 'Población infantil a cargo del ICBF'),
        ('Grupo poblacional no definido', 'Grupo poblacional no definido'),
        ('Madres comunitarias', 'Madres comunitarias'),
        ('Artistas/autores', 'Artistas/autores'),
        ('Otro grupo poblacional', 'Otro grupo poblacional'),
        ('Menores desvinculados', 'Menores desvinculados del conflicto armado bajo protección del ICBF'),
        ('Población discapacitada', 'Población discapacitada'),
    ]
    
    EQUIPO_BASICO_CHOICES = [
        ('EBS #4', 'EBS #4'),
        ('EBS #5', 'EBS #5'),
        ('EBS #6', 'EBS #6'),
    ]

    profesional = models.CharField("Profesional que digita la información", max_length=100)
    fecha_elaboracion = models.DateField("Fecha de elaboración")
    regimen = models.CharField("Régimen", max_length=20, choices=REGIMEN_CHOICES)
    fecha_atencion = models.DateField("Fecha de atención")
    tipo_identificacion = models.CharField("Tipo de identificación", max_length=50)
    numero_identificacion = models.CharField("Número de identificación", max_length=20)
    primer_apellido = models.CharField("Primer apellido", max_length=100)
    segundo_apellido = models.CharField("Segundo apellido", max_length=100, blank=True, null=True)
    primer_nombre = models.CharField("Primer nombre", max_length=100)
    segundo_nombre = models.CharField("Segundo nombre", max_length=100, blank=True, null=True)
    fecha_nacimiento = models.DateField("Fecha de nacimiento")
    sexo = models.CharField("Sexo", max_length=1, choices=SEXO_CHOICES)
    grupo_poblacional = models.CharField("Grupo poblacional", max_length=100, choices=GRUPO_POBLACIONAL_CHOICES)
    etnia = models.CharField("Pertenencia étnica", max_length=1, choices=ETNIA_CHOICES)
    pais_origen = models.CharField("País de origen", max_length=100)
    codigo_zona = models.CharField("Código de zona territorial", max_length=10)
    direccion = models.TextField("Dirección")
    telefono = models.CharField("Teléfono", max_length=15)
    barrio = models.CharField("Barrio / Comunidad", max_length=100)
    microterritorio = models.CharField("Microterritorio", max_length=100)
    subcodigo = models.CharField("Subcódigo", max_length=50)
    descripcion_intervencion = models.TextField("Descripción de la intervención")
    nombre_estrategia = models.CharField("Nombre de la estrategia", max_length=100)
    prioridad_salud = models.CharField("Prioridad en salud", max_length=100)
    equipo_basico = models.CharField("Equipo básico", max_length=10, choices=EQUIPO_BASICO_CHOICES)
    entorno = models.CharField("Entorno", max_length=100)
    observacion = models.TextField("Observación", blank=True, null=True)

    def __str__(self):
        return f"{self.primer_nombre} {self.primer_apellido} - {self.numero_identificacion}"