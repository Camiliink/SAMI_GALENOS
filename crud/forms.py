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
        widgets = {
            'nombre_paciente': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'patient-name',
                'placeholder': 'Nombre completo del paciente',
                'required': True
            }),
            'rut': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'rut',
                'placeholder': 'RUT del paciente',
                'required': True
            }),
            'fecha': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'date',
                'placeholder': 'Seleccione una fecha',
                'readonly': True,
                'required': True
            }),
            'hora': forms.TimeInput(attrs={
                'class': 'form-control',
                'id': 'hora',
                'required': True
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'id': 'email',
                'placeholder': 'Correo electrónico',
                'required': True
            }),
        }

    especialidad = forms.ModelChoiceField(
        queryset=EspecialidadMedico.objects.all(),
        empty_label="Seleccione una especialidad",
        widget=forms.Select(attrs={
            'class': 'form-select',
            'id': 'id_especialidad',
            'onchange': "this.form.submit()"
        }),
        label="Especialidad",
    )

    medico = forms.ModelChoiceField(
        queryset=Usuario.objects.filter(tipo_usuario='medico'),
        empty_label="Seleccione un médico",
        widget=forms.Select(attrs={
            'class': 'form-select',
            'id': 'doctor',
        }),
        label="Médico",
    )

    centro_medico = forms.ModelChoiceField(
        queryset=CentroMedico.objects.all(),
        empty_label="Seleccione un centro médico",
        widget=forms.Select(attrs={
            'class': 'form-select',
            'id': 'centro_medico',
        }),
        label="Centro Médico"
    )

    def __init__(self, *args, **kwargs):
        especialidad = kwargs.pop('especialidad', None)
        super().__init__(*args, **kwargs)

        if especialidad:
            self.fields['medico'].queryset = Usuario.objects.filter(
                tipo_usuario='medico', especialidadmedico__especialidad=especialidad
            )