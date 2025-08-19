from django.db import models

# Modelo de dados dos Clientes
class Client(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nome do Responsável")
    gender = models.CharField(max_length=10, choices=[('M', 'Masculino'), ('F', 'Feminino'), ('O', 'Outro')], verbose_name="Gênero do Responsável")
    phone = models.CharField(max_length=15, verbose_name="Telefone do Responsável")
    email = models.EmailField(max_length=100, verbose_name="Email do Responsável")
    address = models.CharField(max_length=255, verbose_name="Endereço do Responsável")
    cpf = models.CharField(max_length=11, unique=True, verbose_name="CPF do Responsável")
    date_of_birth = models.DateField(verbose_name="Data de Nascimento")
    date_created = models.DateTimeField(auto_now_add=True, verbose_name="Data de Criação")

    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"
        ordering = ['name']

    def __str__(self):
        return self.name