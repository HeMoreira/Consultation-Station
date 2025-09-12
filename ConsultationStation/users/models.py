#from multiprocessing.managers import BaseManager
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

# Gerenciador personalizado para o modelo de Usuários
class UserManager(BaseUserManager):
    # define a lógica de criação de usuários padrão
    def create_user(self, email, password=None, **extra_fields):

        # exige a definição de email e senha
        if not email:
            raise ValueError('O campo de email deve ser preenchido')
        if not password:
            raise ValueError('O campo de senha deve ser preenchido')
        
        # salva o usuário no banco de dados de forma segura
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user
    
    # define a lógica de criação de superusuários
    def create_superuser(self, email, password=None, **extra_fields):

        # permite à superusuários ter permissões administrativas
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        return self.create_user(email, password, **extra_fields)
    
# Modelo de dados dos Usuários
class User(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(max_length=100, verbose_name="Nome Completo")
    gender = models.CharField(max_length=10, choices=[('M', 'Masculino'), ('F', 'Feminino'), ('O', 'Outro')], verbose_name="Gênero")
    phone = models.CharField(max_length=15, verbose_name="Telefone")
    email = models.EmailField(unique=True, verbose_name="Emaail")
    address = models.CharField(max_length=255, verbose_name="Endereço")
    cpf = models.CharField(max_length=11, unique=True, verbose_name="CPF")
    date_of_birth = models.DateField(null=True, verbose_name="Data de Nascimento")
    date_created = models.DateTimeField(auto_now_add=True, verbose_name="Data de Criação")
    is_active = models.BooleanField(default=True, verbose_name="Conta Ativa")
    is_staff = models.BooleanField(default=False, verbose_name="Membro da Equipe")

    # Define o gerenciador personalizado para o modelo de Usuários
    objects = UserManager()

    # Define o campo de email como autenticação para contas
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'cpf']

    class Meta:
        verbose_name = "Usuário"
        verbose_name_plural = "Usuários"
        ordering = ['name']

    def __str__(self):
        return self.name
