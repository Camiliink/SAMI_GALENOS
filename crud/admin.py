from django.contrib import admin
from .models import Usuario,Especialidad_medico, ReservarCita


# Register your models here.

admin.site.register(Usuario)

admin.site.register(Especialidad_medico)

admin.site.register(ReservarCita)