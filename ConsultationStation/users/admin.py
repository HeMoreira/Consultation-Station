from django.contrib import admin
from .models import User

# Registrando o modelo de Usuarios no admin
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('is_active', 'cpf', 'name', 'gender', 'date_of_birth', 'email', 'phone', 'date_created')
    list_filter = ('cpf', 'name', )
    search_fields = ('cpf', 'name')
    ordering = ('-date_created',)