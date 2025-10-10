from django.test import TestCase
from django.contrib.auth import get_user_model
from django.db import IntegrityError, transaction
from django.core.exceptions import ValidationError

# Obtém o modelo de usuário ativo no projeto (seu User personalizado)
User = get_user_model()

# Testes para o UserManager
class UserManagerTest(TestCase):

    # Testa a criação de um usuário padrão
    def test_user_creation(self):
        user_data = {
            'email': 'pedrinhogamer@exemplo.com',
            'password': 'umaSenhaSegura123',
            'name': 'Pedrinho Gamer',
            'cpf': '12345678901',
        }
        user = User.objects.create_user(**user_data)
        self.assertEqual(user.email, user_data['email'])
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)
        self.assertTrue(user.is_active)
        # Garante que a senha foi "hashed" corretamente
        self.assertTrue(user.check_password(user_data['password']))
        # Verifica se os REQUIRED_FIELDS foram salvos
        self.assertEqual(user.name, user_data['name'])

    # Testa a criação de usuário sem email
    def test_user_creation_without_email(self):
        # Dados sem email
        user_data = {
            'email': '',
            'password': 'sememail123',
            'name': 'Nome de Alguém sem Email',
            'cpf': '11122233344',
        }
        # Espera por um ValueError causado pela ausência de email
        with self.assertRaisesMessage(ValueError, 'O campo de email deve ser preenchido'):
            User.objects.create_user(**user_data)
    
    # Testa a criação de usuário sem senha
    def test_user_creation_without_password(self):
        # Dados sem senha
        user_data = {
            'email': 'semsenha@exemplo.com',
            'name': 'Nome',
            'cpf': '11122233344',
        }
        # Espera por um ValueError causado pela ausência de senha
        with self.assertRaisesMessage(ValueError, 'O campo de senha deve ser preenchido'):
            User.objects.create_user(**user_data)

    # Testa a criação de um superusuário
    def test_superuser_creation(self):
        superuser_data = {
            'email': 'superuser@exemplo.com',
            'password': 'senhaSuperSegura',
            'name': 'Admin Daora',
            'cpf': '99988877766',
        }
        superuser = User.objects.create_superuser(**superuser_data)
        self.assertEqual(superuser.email, superuser_data['email'])
        self.assertTrue(superuser.is_staff)
        self.assertTrue(superuser.is_superuser)
        self.assertTrue(superuser.is_active)
        self.assertTrue(superuser.check_password(superuser_data['password']))

# Testes para o modelo User
class UserModelTest(TestCase):
    # Cria um usuário de exemplo para testes de instância
    def setUp(self):
        self.user_data = {
            'email': 'enzogabriel@exemplo.com',
            'password': 'senhaForte456',
            'name': 'Enzo Gabriel',
            'gender': 'M',
            'phone': '11999999999',
            'address': 'Av. Teste, 456 - XD',
            'cpf': '11122233344',
        }
        self.user = User.objects.create_user(**self.user_data)

    # Testa a representação em string do usuário
    def test_str_representation(self):
        self.assertEqual(str(self.user), 'Enzo Gabriel')

    # Testa os campos do usuário criado
    def test_user_creation_fields(self):
        self.assertEqual(self.user.email, self.user_data['email'])
        self.assertEqual(self.user.name, self.user_data['name'])
        self.assertEqual(self.user.phone, self.user_data['phone'])
        self.assertEqual(self.user.address, self.user_data['address'])
        self.assertEqual(self.user.cpf, self.user_data['cpf'])
        self.assertEqual(self.user.gender, self.user_data['gender'])

    # Garante que o email e o cpf são únicos
    def test_unique_fields_integrity(self):
        # Cria um segundo usuário com o mesmo email em busca de IntegrityError
        with transaction.atomic():
            with self.assertRaises(IntegrityError):
                User.objects.create_user(
                    email=self.user_data['email'], # Email duplicado
                    password='outrasenha',
                    phone='11888888888',
                    address='Rua Etset, 789',
                    name='Outro Enzo',
                    cpf='00011122233',
                    gender='O',
                )
        
        # Tenta criar um segundo usuário com o mesmo CPF
        with transaction.atomic():
            with self.assertRaises(IntegrityError):
                User.objects.create_user(
                    email='novoemail@site.com',
                    password='outrasenha',
                    phone='11888888888',
                    address='Rua Etset, 789',
                    name='Uma Enza',
                    cpf=self.user_data['cpf'], # CPF duplicado
                    gender='F',
                )
