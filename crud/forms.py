# En forms.py
from django import forms
from .models import Usuario, TIPO_USUARIO_CHOICES, ReservarCita, EspecialidadMedico,CentroMedico
from django import forms

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = '__all__'
        widgets = {
            'tipo_usuario': forms.Select(
                choices=TIPO_USUARIO_CHOICES,
                attrs={
                    'class': 'form-select',  
                }
            ),
            'rut': forms.TextInput(attrs={'class': 'form-control'}),
            'nombre_usuario': forms.TextInput(attrs={'class': 'form-control'}),
            'nombre_completo': forms.TextInput(attrs={'class': 'form-control'}),
            'correo': forms.EmailInput(attrs={'class': 'form-control'}),
            'contrasenna': forms.PasswordInput(attrs={'class': 'form-control'}),
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



class ReservaCitaForm(forms.ModelForm):
    class Meta:
        model = ReservarCita
        fields = ['especialidad', 'medico', 'nombre_paciente', 'rut', 'fecha', 'hora', 'email', 'centro_medico']

    especialidad = forms.ModelChoiceField(
        queryset=EspecialidadMedico.objects.none(),
        empty_label="Seleccionar Especialidad",
        widget=forms.Select(attrs={'class': 'form-select'}),
        label="Especialidad",
    )

    medico = forms.ModelChoiceField(
        queryset=Usuario.objects.filter(tipo_usuario='medico'),
        empty_label="Seleccionar Médico",
        widget=forms.Select(attrs={'class': 'form-select'}),
        label="Médico",
    )

    centro_medico = forms.ChoiceField(
        choices=[('', 'Seleccionar Centro Médico')] + CentroMedico.CENTRO_MEDICO_CHOICES,
        widget=forms.Select(attrs={'class': 'form-select'}),
        label="Centro Médico",
    )

    def __init__(self, *args, **kwargs):
        especialidad = kwargs.pop('especialidad', None)  # Filtrar especialidad si es pasada
        super().__init__(*args, **kwargs)
        # Si hay una especialidad, filtrar las opciones
        if especialidad:
            self.fields['especialidad'].queryset = EspecialidadMedico.objects.filter(especialidad=especialidad)
            self.fields['medico'].queryset = Usuario.objects.filter(
                tipo_usuario='medico',
                especialidadmedico__especialidad=especialidad
            )
        else:
            # Si no hay especialidad seleccionada, mostrar todas las especialidades
            self.fields['especialidad'].queryset = EspecialidadMedico.objects.all()