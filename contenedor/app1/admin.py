from django.contrib import admin
from .models import Turno

class Turno_Admin(admin.ModelAdmin):
    fields = ["nombre_cliente", "apellido_cliente", "email", "telefono", "fecha", "hora"]
    list_display = ["nombre_cliente", "apellido_cliente", "fecha", "hora"]  # Corregido a "apellido_cliente"

admin.site.register(Turno, Turno_Admin)
