from django.contrib import admin
from .models import Usuario, EspecialidadMedico, ReservarCita,CentroMedico


# Register your models here.

admin.site.register(Usuario)
admin.site.register(EspecialidadMedico)
admin.site.register(ReservarCita)
admin.site.register(CentroMedico)