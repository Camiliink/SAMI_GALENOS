from django.db import models

# Opciones de tipo de usuario
TIPO_USUARIO_CHOICES = [
    ('medico', 'Médico'),
    ('paciente', 'Paciente'),
    ('administrador', 'Administrador'),
    ('cajera', 'Cajera'),
    ('secretaria', 'Secretaria'),
]

class Usuario(models.Model):
    code = models.AutoField(primary_key=True, verbose_name="codigo")
    rut = models.CharField(max_length=12, db_index=True)
    nombre_usuario = models.CharField(max_length=20, verbose_name="Nombre Usuario")
    nombre_completo = models.CharField(max_length=50, verbose_name="Nombre Completo")
    correo = models.EmailField(max_length=100, blank=True, null=True)  # Campo de correo
    contrasenna = models.CharField(max_length=20, verbose_name="Contraseña")
    tipo_usuario = models.CharField(max_length=20, choices=TIPO_USUARIO_CHOICES, verbose_name="Tipo Usuario")
    
    def save(self, *args, **kwargs):
        # Genera el correo automáticamente a partir del nombre completo
        if not self.correo:  # Si no se proporciona correo, lo genera
            self.correo = f"{self.nombre_completo.replace(' ', '').lower()}@gmail.com"
        super(Usuario, self).save(*args, **kwargs)

    def __str__(self):
        return f"Nombre: {self.nombre_completo} - Nombre Usuario: {self.nombre_usuario} - Tipo Usuario: {self.tipo_usuario}"

class Especialidad_medico(models.Model):
    ESPECIALIDAD_CHOICES = [
        ('cardiologia', 'Cardiología'),
        ('pediatria', 'Pediatría'),
        ('dermatologia', 'Dermatología'),
        # Agregar más especialidades según sea necesario
    ]
    
    medico = models.CharField(
        max_length=50, 
        choices=[(user.nombre_completo, user.nombre_completo) for user in Usuario.objects.filter(tipo_usuario='medico')],
        verbose_name="Médico"
    )
    
    especialidad = models.CharField(
        max_length=50, 
        choices=ESPECIALIDAD_CHOICES, 
        verbose_name="Especialidad"
    )
    
    def __str__(self):
        return f"{self.medico} - {self.especialidad}"

    class Meta:
        verbose_name = "Especialidad del Médico"
        verbose_name_plural = "Especialidades de los Médicos"

class CentroMedico(models.Model):
    CENTRO_MEDICO_CHOICES = [
        ('centro1', 'Centro Médico 1'),
        ('centro2', 'Centro Médico 2'),
        ('centro3', 'Centro Médico 3'),
        # Agregar más centros médicos según sea necesario
    ]
    nombre = models.CharField(max_length=50, choices=CENTRO_MEDICO_CHOICES, verbose_name="Centro Médico")
    
    def __str__(self):
        return self.nombre

class ReservarCita(models.Model):
    # Usamos CharField para almacenar solo el nombre completo del médico
    medico = models.CharField(
        max_length=50, 
        choices=[(user.nombre_completo, user.nombre_completo) for user in Usuario.objects.filter(tipo_usuario='medico')],
        verbose_name="Médico"
    )

    nombre_paciente = models.CharField(max_length=100)
    rut = models.CharField(max_length=12, unique=True) # RUT del paciente
    fecha = models.DateField()
    hora = models.TimeField()
    especialidad = models.CharField(max_length=50, choices=Especialidad_medico.ESPECIALIDAD_CHOICES)
    email = models.EmailField()
    
    # Relación con Centro Médico
    centro_medico = models.ForeignKey(
        CentroMedico, 
        on_delete=models.CASCADE,
        verbose_name="Centro Médico"
    )

    def __str__(self):
        return f"Cita de {self.nombre_paciente} para {self.especialidad} con {self.medico} en {self.centro_medico.nombre}"
