from django.urls import path
from django.conf import settings
from django.contrib.staticfiles.urls import static
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('nosotros', views.nosotros, name='nosotros'),
    path('usuarios', views.usuarios, name='usuarios'),
    path('hora', views.hora, name='hora'),
    path('usuarios/crear', views.crear, name='crear'),
    path('usuarios/editar', views.editar, name='editar'),
    path('eliminar/<int:code>', views.eliminar,name='eliminar'),
    path('usuarios/editar/<int:code>', views.editar, name='editar'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
 