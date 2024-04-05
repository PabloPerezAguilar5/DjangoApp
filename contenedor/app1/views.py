from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Turno
from .google_calendar_manager import GoogleCalendarManager  
import datetime
from django.http import HttpResponseBadRequest


SCOPES = ["https://www.googleapis.com/auth/calendar"]


def IndexView(request):
    # Lógica para la vista de la página principal
    return render(request, 'index.html')

def reservar_turno(request):
    if request.method == 'POST':
        # Obtener los datos del formulario
        nombre_cliente = request.POST.get('nombre_cliente')
        apellido_cliente = request.POST.get('apellido_cliente')
        email = request.POST.get('email')
        telefono = request.POST.get('telefono')
        fecha = request.POST.get('fecha')
        hora = request.POST.get('hora')

        # Crear un nuevo objeto Turno y guardarlo en la base de datos
        nuevo_turno = Turno(
            nombre_cliente=nombre_cliente,
            apellido_cliente=apellido_cliente,
            email=email,
            telefono=telefono,
            fecha=fecha,
            hora=hora
        )
        nuevo_turno.save()

        # Redirigir a una página de confirmación o a donde desees
        return redirect(reverse('confirmacion_turno'))

    # Si no es una solicitud POST, renderizamos el formulario de registro de turno
    return render(request, 'formulario_turno.html')


def confirmacion_turno(request):
    # Lógica para la página de confirmación de turno
    return render(request, 'confirmacion_turno.html')





