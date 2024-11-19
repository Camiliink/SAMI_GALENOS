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
class LoginForm(forms.Form):
    nombre_usuario = forms.CharField(
        label='Nombre de Usuario',
        max_length=20,
        widget=forms.TextInput(attrs={'placeholder': 'Nombre de usuario'}),
    )
    contrasenna = forms.CharField(
        label='Contraseña',
        max_length=20,
        widget=forms.PasswordInput(attrs={'placeholder': 'Contraseña'}),
    )

    def clean(self):
        cleaned_data = super().clean()
        nombre_usuario = cleaned_data.get("nombre_usuario")
        contrasenna = cleaned_data.get("contrasenna")

        # Validación de usuario
        if not Usuario.objects.filter(nombre_usuario=nombre_usuario, contrasenna=contrasenna).exists():
            raise forms.ValidationError("Usuario o contraseña incorrectos.")
        return cleaned_data