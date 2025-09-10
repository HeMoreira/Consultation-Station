from django.db import models
from doctors.models import Doctor
from users.models import User

# Modelo de dados das Consultas
class Consultation(models.Model):
    patient_name = models.CharField(max_length=100, verbose_name="Paciente")
    user_account = models.ForeignKey(User, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    date = models.DateTimeField(verbose_name="Data da Consulta")
    description = models.TextField(max_length=200, verbose_name="Descrição da Consulta")
    duration = models.IntegerField(default=30)
    date_created = models.DateTimeField(auto_now_add=True, verbose_name="Data de Criação")

    class Meta:
        verbose_name = "Consulta"
        verbose_name_plural = "Consultas"
        ordering = ['-date']

    def __str__(self):
        return f"{self.patient_name} - {self.doctor.name}"