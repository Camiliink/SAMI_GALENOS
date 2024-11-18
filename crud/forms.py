# En forms.py
from django import forms
from .models import Usuario, TIPO_USUARIO_CHOICES  # Importa el listado de opciones

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = '__all__'
        widgets = {
            'tipo_usuario': forms.Select(choices=TIPO_USUARIO_CHOICES),  # Aquí usas las opciones importadas
        }
