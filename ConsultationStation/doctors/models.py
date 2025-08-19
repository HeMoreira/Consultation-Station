from django.db import models

# Modelo de dados dos Médicos
class Doctor(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nome do Médico")
    specialty = models.CharField(max_length=50, verbose_name="Especialidade")
    gender = models.CharField(max_length=10, choices=[('M', 'Masculino'), ('F', 'Feminino'), ('O', 'Outro')], verbose_name="Gênero do Médico")
    phone = models.CharField(max_length=15, verbose_name="Telefone do Médico")
    email = models.EmailField(max_length=100, verbose_name="Email do Médico")
    address = models.CharField(max_length=255, verbose_name="Endereço do Médico")
    cpf = models.CharField(max_length=11, unique=True, verbose_name="CPF do Médico")
    date_of_birth = models.DateField(verbose_name="Data de Nascimento")
    date_created = models.DateTimeField(auto_now_add=True, verbose_name="Data de Criação")

    class Meta:
        verbose_name = "Médico"
        verbose_name_plural = "Médicos"
        ordering = ['name']

    def __str__(self):
        return f"{self.specialty} - {self.name}"