from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import UsuarioForm
from .forms import LoginForm
from .forms import ReservaCitaForm
from django.contrib import messages  
from .models import  ReservarCita, EspecialidadMedico, Usuario, CentroMedico

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            # Validar usuario y guardar su tipo en la sesión
            nombre_usuario = form.cleaned_data.get('nombre_usuario')
            contrasenna = form.cleaned_data.get('contrasenna')
            try:
                usuario = Usuario.objects.get(nombre_usuario=nombre_usuario, contrasenna=contrasenna)
                request.session['tipo_usuario'] = usuario.tipo_usuario  # Guardar tipo de usuario en sesión
                return redirect('inicio')   # Redirigir a la página de inicio
            except Usuario.DoesNotExist:
                form.add_error(None, "Usuario o contraseña incorrectos")
        return render(request, 'paginas/login.html', {'form': form})
    else:
        form = LoginForm()
    return render(request, 'paginas/login.html', {'form': form})

def inicio(request):
    return render(request, 'paginas/inicio.html')
def nosotros(request):
    return render(request, 'paginas/nosotros.html')
def hora(request):
    return render(request, 'paginas/hora.html')
from django.shortcuts import render
from .models import Usuario

def usuarios(request):
    # Obtener el parámetro de búsqueda del RUT
    busqueda_rut = request.GET.get('buscar_rut', '').strip()

    if busqueda_rut:
        # Primero busca el usuario con el RUT exacto
        usuarios_exactos = Usuario.objects.filter(rut=busqueda_rut)

        # Luego busca los usuarios que contengan el RUT (sin distinción de mayúsculas/minúsculas)
        usuarios_restantes = Usuario.objects.filter(rut__icontains=busqueda_rut).exclude(rut=busqueda_rut)

        # Combina ambos conjuntos de usuarios, primero los exactos, luego los demás
        usuarios = list(usuarios_exactos) + list(usuarios_restantes)
    else:
        # Si no hay búsqueda, mostrar todos los usuarios
        usuarios = Usuario.objects.all()

    # Renderiza la plantilla pasando los usuarios y la búsqueda
    return render(request, 'usuarios/index.html', {'usuarios': usuarios, 'busqueda_rut': busqueda_rut})

def crear(request):
    print('entró a crear')
    print(request.POST)
    formulario = UsuarioForm(request.POST or None, request.FILES or None)

    print(formulario.errors)
    if formulario.is_valid():
        print('formulario valido')
        formulario.save()
        return redirect('usuarios')
        
    return render(request, 'usuarios/crear.html', {'formulario': formulario})

def editar(request,code):
    usuario = Usuario.objects.get(code=code)
    formulario = UsuarioForm(request.POST or None, request.FILES or None, instance=usuario)
    
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('usuarios')

    return render(request, 'usuarios/editar.html',{'formulario': formulario})

def eliminar(request,code):
    usuario= Usuario.objects.get(code=code)
    usuario.delete()
    return redirect('usuarios')

def cerrar_sesion(request):
    request.session.flush()
    return redirect('login')

def hora(request):
    # Obtener parámetros de la URL (con None por defecto en lugar de '')
    especialidad_seleccionada = request.GET.get('especialidad', None)
    doctor_seleccionado = request.GET.get('doctor', None)

    # Obtener todos los centros médicos
    centros_medicos = CentroMedico.objects.all()

    # Obtener todas las especialidades disponibles
    especialidades = EspecialidadMedico.ESPECIALIDAD_CHOICES

    # Filtrar médicos según la especialidad seleccionada
    medicos = Usuario.objects.filter(tipo_usuario='medico')
    if especialidad_seleccionada:
        medicos = medicos.filter(especialidadmedico__especialidad=especialidad_seleccionada)

    # Filtrar médicos según el doctor seleccionado
    if doctor_seleccionado:
        medicos = medicos.filter(id=doctor_seleccionado)

    # Verificar si no hay médicos disponibles
    no_medicos_disponibles = not medicos.exists()

    # Manejar formulario de reserva
    if request.method == "POST":
        formulario = ReservaCitaForm(request.POST)
        if formulario.is_valid():
            # Guardar la reserva en la base de datos
            formulario.save()

            # Mensaje de éxito
            messages.success(request, "Cita reservada con éxito.")

            # Redirigir a la misma página u otra URL
            return redirect('hora')  # Cambia 'hora' por el nombre de tu URL si es necesario
        else:
            messages.error(request, "Por favor, corrige los errores en el formulario.")
    else:
        formulario = ReservaCitaForm(initial={
            'especialidad': especialidad_seleccionada,
            'medico': doctor_seleccionado,
        })

    # Renderizar la plantilla con el contexto
    return render(request, 'paginas/hora.html', {
        'formulario': formulario,
        'medicos': medicos,
        'especialidades': especialidades,
        'especialidad_seleccionada': especialidad_seleccionada,
        'doctor_seleccionado': doctor_seleccionado,
        'centros_medicos': centros_medicos,
        'no_medicos_disponibles': no_medicos_disponibles,
    })