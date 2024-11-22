from django.contrib import admin
from .models import Usuario, EspecialidadMedico, ReservarCita


# Register your models here.

admin.site.register(Usuario)
admin.site.register(EspecialidadMedico)
admin.site.register(ReservarCita)