from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Turno
from django.core.mail import send_mail
import os
import smtplib



SCOPES = ["https://www.googleapis.com/auth/calendar"]


def IndexView(request):
    # Lógica para la vista de la página principal
    return render(request, 'index.html')

def reservar_turno(request):
    if request.method == 'POST':
        # Obtain the form data
        nombre_cliente = request.POST.get('nombre_cliente')
        apellido_cliente = request.POST.get('apellido_cliente')
        email = request.POST.get('email')
        telefono = request.POST.get('telefono')
        fecha = request.POST.get('fecha')
        hora = request.POST.get('hora')

        # Create a new Turno object and save it in the database
        nuevo_turno = Turno(
            nombre_cliente=nombre_cliente,
            apellido_cliente=apellido_cliente,
            email=email,
            telefono=telefono,
            fecha=fecha,
            hora=hora
        )
        nuevo_turno.save()

        # Get the email of the last Turno created
        ultimo_turno = Turno.objects.latest('id')
        email = ultimo_turno.email

        # Set up the email content
        subject = 'Turno Confirmado'
        message = 'Su turno ha sido confirmado para el día {} a las {}. Gracias por reservar con nosotros.'.format(fecha, hora)

        # Set up the email sender
        sender = 'pabloperezaguilar@gmail.com'

        # Send the email
        send_mail(subject, message, sender, [email])

        # Optionally, you can also print a message to the console for debugging purposes
        print('Confirmation email sent to', email)

        # Redirect to the confirmation page
        return redirect('confirmacion_turno')

    # If the request method is not POST, render the form page
    return render(request, 'reservar_turno.html')


def confirmacion_turno(request):
    # Lógica para la página de confirmación de turno
    return render(request, 'confirmacion_turno.html')








