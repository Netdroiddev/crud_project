# Generated by Django 5.1.5 on 2025-06-06 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Formulario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profesional', models.CharField(max_length=100, verbose_name='Profesional que digita la información')),
                ('fecha_elaboracion', models.DateField(verbose_name='Fecha de elaboración')),
                ('regimen', models.CharField(choices=[('SUBSIDIADO', 'Subsidiado'), ('CONTRIBUTIVO', 'Contributivo'), ('ESPECIAL', 'Especial o de Excepción'), ('NO_ASEGURADO', 'No Asegurado')], max_length=20, verbose_name='Régimen')),
                ('fecha_atencion', models.DateField(verbose_name='Fecha de atención')),
                ('tipo_identificacion', models.CharField(max_length=50, verbose_name='Tipo de identificación')),
                ('numero_identificacion', models.CharField(max_length=20, verbose_name='Número de identificación')),
                ('primer_apellido', models.CharField(max_length=100, verbose_name='Primer apellido')),
                ('segundo_apellido', models.CharField(blank=True, max_length=100, null=True, verbose_name='Segundo apellido')),
                ('primer_nombre', models.CharField(max_length=100, verbose_name='Primer nombre')),
                ('segundo_nombre', models.CharField(blank=True, max_length=100, null=True, verbose_name='Segundo nombre')),
                ('fecha_nacimiento', models.DateField(verbose_name='Fecha de nacimiento')),
                ('sexo', models.CharField(choices=[('M', 'Masculino'), ('F', 'Femenino')], max_length=1, verbose_name='Sexo')),
                ('grupo_poblacional', models.CharField(choices=[('Indigentes', 'Indigentes'), ('Población infantil vulnerable', 'Población infantil vulnerable bajo protección en instituciones diferentes a ICBF'), ('Personas en protección a testigos', 'Personas en protección a testigos'), ('Población en centros psiquiátricos', 'Población en centros psiquiátricos'), ('Población rural migratoria', 'Población rural migratoria'), ('Población en centros carcelarios', 'Población en centros carcelarios'), ('Población rural no migratoria', 'Población rural no migratoria'), ('Adultos mayores en centros de protección', 'Adultos mayores en centros de protección'), ('Comunidades indígenas', 'Comunidades indígenas'), ('Población ROM', 'Población ROM'), ('Afrocolombianos', 'Afrocolombianos'), ('Población infantil ICBF', 'Población infantil a cargo del ICBF'), ('Grupo poblacional no definido', 'Grupo poblacional no definido'), ('Madres comunitarias', 'Madres comunitarias'), ('Artistas/autores', 'Artistas/autores'), ('Otro grupo poblacional', 'Otro grupo poblacional'), ('Menores desvinculados', 'Menores desvinculados del conflicto armado bajo protección del ICBF'), ('Población discapacitada', 'Población discapacitada')], max_length=100, verbose_name='Grupo poblacional')),
                ('etnia', models.CharField(choices=[('1', 'Indígena'), ('2', 'ROM'), ('3', 'Raizal'), ('4', 'Palenquero'), ('5', 'Afrodescendiente'), ('6', 'Otras etnias'), ('Z', 'Sin identificar')], max_length=1, verbose_name='Pertenencia étnica')),
                ('pais_origen', models.CharField(max_length=100, verbose_name='País de origen')),
                ('codigo_zona', models.CharField(max_length=10, verbose_name='Código de zona territorial')),
                ('direccion', models.TextField(verbose_name='Dirección')),
                ('telefono', models.CharField(max_length=15, verbose_name='Teléfono')),
                ('barrio', models.CharField(max_length=100, verbose_name='Barrio / Comunidad')),
                ('microterritorio', models.CharField(max_length=100, verbose_name='Microterritorio')),
                ('subcodigo', models.CharField(max_length=50, verbose_name='Subcódigo')),
                ('descripcion_intervencion', models.TextField(verbose_name='Descripción de la intervención')),
                ('nombre_estrategia', models.CharField(max_length=100, verbose_name='Nombre de la estrategia')),
                ('prioridad_salud', models.CharField(max_length=100, verbose_name='Prioridad en salud')),
                ('equipo_basico', models.CharField(choices=[('EBS #4', 'EBS #4'), ('EBS #5', 'EBS #5'), ('EBS #6', 'EBS #6')], max_length=10, verbose_name='Equipo básico')),
                ('entorno', models.CharField(max_length=100, verbose_name='Entorno')),
                ('observacion', models.TextField(blank=True, null=True, verbose_name='Observación')),
            ],
        ),
    ]
