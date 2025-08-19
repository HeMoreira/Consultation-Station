from django.contrib import admin
from .models import Doctor

# Registrando o modelo de Médicos no admin
@admin.register(Doctor)
class ConsultationAdmin(admin.ModelAdmin):
    list_display = ('cpf', 'name', 'specialty', 'phone', 'email', 'date_of_birth', 'date_created')
    list_filter = ('cpf', 'name', 'specialty')
    search_fields = ('cpf', 'name', 'specialty')
    ordering = ('specialty',)