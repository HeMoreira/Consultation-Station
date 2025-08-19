from django.contrib import admin
from .models import Client

# Registrando o modelo de Clientes no admin
@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('cpf', 'name', 'gender', 'date_of_birth', 'email', 'phone', 'date_created')
    list_filter = ('cpf', 'name')
    search_fields = ('cpf', 'name')
    ordering = ('-date_created',)