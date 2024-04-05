from django.urls import path
from .views import reservar_turno, confirmacion_turno

urlpatterns = [
    path('reservar_turno/', reservar_turno, name='reservar_turno'),
    path('confirmacion_turno/', confirmacion_turno, name='confirmacion_turno'),
    # Otras rutas URL específicas de la aplicación...
]
