from django.contrib import admin
from .models import Consultation

# Registrando o modelo de Consultas no admin
@admin.register(Consultation)
class ConsultationAdmin(admin.ModelAdmin):
    list_display = ('patient_name', 'doctor', 'date', 'date_created')
    list_filter = ('date', 'doctor')
    search_fields = ('patient_name',)
    ordering = ('-date',)
    date_hierarchy = 'date'