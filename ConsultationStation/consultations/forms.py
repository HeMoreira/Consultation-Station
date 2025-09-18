from django import forms
from .models import Consultation

# Formulário para criação de novas consultas
class ConsultationForm(forms.ModelForm):
    patient_name = forms.CharField(label="Nome do Paciente", max_length=100, widget=forms.TextInput(attrs={'size': 50}))
    date = forms.DateTimeField(label="Horário da Consulta", widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}))
    description = forms.CharField(label="", max_length=200, widget=forms.Textarea(attrs={'placeholder': 'Descreva o motivo da consulta', 'size': 60, 'rows': 4}))
    duration = forms.IntegerField(label="Duração (minutos)", initial=30, min_value=30, max_value=120)

    class Meta:
        model = Consultation
        fields = ['patient_name', 'doctor', 'date', 'description', 'duration']
