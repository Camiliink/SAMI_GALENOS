from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Usuario
from .forms import UsuarioForm
# Create your views here.

def inicio(request):
    return render(request, 'paginas/inicio.html')
def nosotros(request):
    return render(request, 'paginas/nosotros.html')
def hora(request):
    return render(request, 'paginas/hora.html')
def usuarios(request):
    usuarios= Usuario.objects.all()

    return render(request, 'usuarios/index.html', {'usuarios': usuarios})

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