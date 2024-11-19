from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.login, name='login'),
    path('login/', views.login, name='login'),
    path('inicio/', views.inicio, name='inicio'),  # Página principal
    path('nosotros', views.nosotros, name='nosotros'),  # Página de "Nosotros"
    path('usuarios', views.usuarios, name='usuarios'),  # Lista de usuarios
    path('hora', views.hora, name='hora'),  # Vista de hora
    path('usuarios/crear/', views.crear, name='crear'),  # Crear usuario
    path('usuarios/editar/<int:code>/', views.editar, name='editar'),  # Editar usuario específico
    path('usuarios/eliminar/<int:code>/', views.eliminar, name='eliminar'),  # Eliminar usuario específico
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
