from django.db import models

# Create your models here.
class Usuario(models.Model):
    code = models.AutoField(primary_key=True,verbose_name="codigo")
    rut = models.CharField(max_length=12)
    nombre_usuario = models.CharField(max_length=20,verbose_name="Nombre Usuario")
    nombre_completo = models.CharField(max_length=50,verbose_name="Nombre Completo")
    contrasenna = models.CharField(max_length=20,verbose_name="Contraseña")
    tipo_usuario = models.CharField(max_length=20,verbose_name="Tipo Usuario")
    
    def __str__(self):
        fila = "Nombre: " + self.nombre_completo + " - " + "Nombre Usuario: " + self.nombre_usuario + " - " + "Tipo Usuario: " + self.tipo_usuario
        return fila
    