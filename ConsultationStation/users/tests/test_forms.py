from django.test import TestCase
from ..forms import CustomRegistrationForm, CustomAuthenticationForm
from datetime import date
from ..models import User

class UserFormsTest(TestCase):
    def setUp(self):
        # Define dados válidos para o formulário de registro
        self.form_data = {
            'email': 'pedrojunior@exemplo.com',
            'password1': 'senhaForte456',
            'password2': 'senhaForte456',
            'name': 'Enzo Gabriel',
            'gender': 'M',
            'phone': '11999999999',
            'address': 'Av. Teste, 456 - XD',
            'cpf': '99977788890',
            'date_of_birth': date(1990, 1, 1),
        }
        self.form = CustomRegistrationForm(data=self.form_data)

    # Testa se o formulário de registro é válido quando com dados corretos
    def test_registration_form_valid_data(self):
        # Verifica se o formulário é válido com os dados fornecidos
        self.assertTrue(self.form.is_valid())

    # Testa se o formulário de registro é inválido quando com dados incorretos
    def test_registration_form_invalid_data_name(self):
        # Define dados inválidos para o formulário de registro
        form_data = {
            'email': 'enzogabriel@exemplo.com',
            'password': 'senhaForte456',
            'name': 'a'*101,
            'gender': 'M',
            'phone': '11999999999',
            'address': 'Av. Teste, 456 - XD',
            'cpf': '11122233344',
        }
        form = CustomRegistrationForm(data=form_data)
        # Verifica se o formulário é inválido com os dados fornecidos
        self.assertFalse(form.is_valid())
        # Verifica se o erro está relacionado ao campo 'name' no formulário
        self.assertIn('name', form.errors)

    def test_registration_form_invalid_data_address(self):
        # Define dados inválidos para o formulário de registro
        form_data = {
            'email': 'enzogabriel@exemplo.com',
            'password': 'senhaForte456',
            'name': 'Enzo Gabriel',
            'gender': 'M',
            'phone': '11999999999',
            'address': 'a'*256,
            'cpf': '11122233344',
        }
        form = CustomRegistrationForm(data=form_data)
        # Verifica se o formulário é inválido com os dados fornecidos
        self.assertFalse(form.is_valid())
        # Verifica se o erro está relacionado ao campo 'address' no formulário
        self.assertIn('address', form.errors)

    def test_registration_form_invalid_data_email(self):
        # Define dados inválidos para o formulário de registro
        form_data = {
            'email': 'invalid-email',
            'password': 'senhaForte456',
            'name': 'Enzo Gabriel',
            'gender': 'M',
            'phone': '11999999999',
            'address': 'Av. Teste, 456 - XD',
            'cpf': '11122233344',
        }
        form = CustomRegistrationForm(data=form_data)
        # Verifica se o formulário é inválido com os dados fornecidos
        self.assertFalse(form.is_valid())
        # Verifica se o erro está relacionado ao campo 'email' no formulário
        self.assertIn('email', form.errors)
        # Verifica se o label do campo 'email' está correto
        self.assertEqual(form.fields['email'].label, "Email")

    def test_registration_form_invalid_data_gender(self):
        # Define dados inválidos para o formulário de registro
        form_data = {
            'email': 'enzogabriel@teste.com',
            'password': 'senhaForte456',
            'name': 'Enzo Gabriel',
            'gender': 'M'*2,
            'phone': '11999999999',
            'address': 'Av. Teste, 456 - XD',
            'cpf': '11122233344',
        }
        form = CustomRegistrationForm(data=form_data)
        # Verifica se o formulário é inválido com os dados fornecidos
        self.assertFalse(form.is_valid())
        # Verifica se o erro está relacionado ao campo 'genero' no formulário
        self.assertIn('gender', form.errors)

    def test_registration_form_invalid_data_phone(self):
        # Define dados inválidos para o formulário de registro
        form_data = {
            'email': 'enzogabriel@teste.com',
            'password': 'senhaForte456',
            'name': 'Enzo Gabriel',
            'gender': 'M',
            'phone': 'a'*16,
            'address': 'Av. Teste, 456 - XD',
            'cpf': '11122233344',
        }
        form = CustomRegistrationForm(data=form_data)
        # Verifica se o formulário é inválido com os dados fornecidos
        self.assertFalse(form.is_valid())
        # Verifica se o erro está relacionado ao campo 'genero' no formulário
        self.assertIn('phone', form.errors)

    def test_registration_form_invalid_data_cpf(self):
        # Define dados inválidos para o formulário de registro
        form_data = {
            'email': 'enzogabriel@teste.com',
            'password': 'senhaForte456',
            'name': 'Enzo Gabriel',
            'gender': 'M',
            'phone': '11999999999',
            'address': 'Av. Teste, 456 - XD',
            'cpf': 'a'*12,
        }
        form = CustomRegistrationForm(data=form_data)
        # Verifica se o formulário é inválido com os dados fornecidos
        self.assertFalse(form.is_valid())
        # Verifica se o erro está relacionado ao campo 'genero' no formulário
        self.assertIn('cpf', form.errors)

    # Testa se o formulário de autenticação é válido quando com dados corretos
    def test_authentication_form_valid_data(self):
        # Primeiro, cria um usuário para autenticação
        self.form_data['password'] = self.form_data['password1']
        self.form_data.pop('password1')
        self.form_data.pop('password2')
        User.objects.create_user(**self.form_data)
        # Define dados válidos para o formulário de login com base no registro anterior
        form_login_data = {
            'username': 'pedrojunior@exemplo.com',
            'password': 'senhaForte456',
        }
        self.form_login = CustomAuthenticationForm(data=form_login_data)
        # Verifica se o formulário é válido com os dados fornecidos
        self.assertTrue(self.form_login.is_valid())
    
    # Testa se o formulário de autenticação é inválido quando com dados incorretos
    def test_authentication_form_invalid_data_email(self):
        # Define dados inválidos para o formulário de login
        form_login_data = {
            'username': 'invalid-email',
            'password': 'senhaForte456',
        }
        form = CustomAuthenticationForm(data=form_login_data)
        # Verifica se o formulário é inválido com os dados fornecidos
        self.assertFalse(form.is_valid())
        # Verifica se o erro está relacionado ao campo 'username' no formulário
        self.assertIn('username', form.errors)

    def test_authentication_form_invalid_data_password(self):
        # Define dados inválidos para o formulário de login
        form_login_data = {
            'username': 'enzogabriel@exemplo.com',
            'password': 'SenhaIncorreta321',
        }
        form = CustomAuthenticationForm(data=form_login_data)
        # Verifica se o formulário é inválido com os dados fornecidos
        self.assertFalse(form.is_valid())
        # Verifica se o erro está relacionado ao campo 'password' no formulário
        self.assertIn('__all__', form.errors)