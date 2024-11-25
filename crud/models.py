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

class EspecialidadMedico(models.Model):
    ESPECIALIDAD_CHOICES = [
        ('cardiologia', 'Cardiología'),
        ('pediatria', 'Pediatría'),
        ('dermatologia', 'Dermatología'),
    ]
    
    medico = models.ForeignKey(
        Usuario, 
        limit_choices_to={'tipo_usuario': 'medico'},
        on_delete=models.CASCADE,
        verbose_name="Médico"
    )
    especialidad = models.CharField(
        max_length=50, 
        choices=ESPECIALIDAD_CHOICES, 
        verbose_name="Especialidad"
    )
    
    def __str__(self):
        return f"{self.medico.nombre_completo} - {self.especialidad}"

class CentroMedico(models.Model):

    nombre = models.CharField(max_length=50, verbose_name="Centro Médico")
    
    def __str__(self):
        return self.nombre

class ReservarCita(models.Model):
    medico = models.ForeignKey(
        Usuario,
        limit_choices_to={'tipo_usuario': 'medico'},
        on_delete=models.CASCADE,
        verbose_name="Médico"
    )
    nombre_paciente = models.CharField(max_length=100)
    rut = models.CharField(max_length=12, unique=True) 
    fecha = models.DateField()
    hora = models.TimeField()
    especialidad = models.ForeignKey(
        EspecialidadMedico,
        on_delete=models.CASCADE,
        verbose_name="Especialidad"
    )
    email = models.EmailField()
    centro_medico = models.ForeignKey(
        CentroMedico, 
        on_delete=models.CASCADE,
        verbose_name="Centro Médico"
    )

    def __str__(self):
        return f"Cita de {self.nombre_paciente} para {self.especialidad} con {self.medico} en {self.centro_medico.nombre}"