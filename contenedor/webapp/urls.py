from django.contrib import admin
from django.urls import path, include
from app1.views import IndexView, reservar_turno, confirmacion_turno

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView, name='index'),  # Ruta para la URL raíz
    path('reservar_turno/', reservar_turno, name='reservar_turno'),  # Ruta para reservar_turno
    path('confirmacion_turno/', confirmacion_turno, name='confirmacion_turno'),  # Ruta para confirmacion_turno
]
