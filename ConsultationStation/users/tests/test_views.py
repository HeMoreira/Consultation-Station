from django.test import TestCase
from django.urls import reverse
from ..models import User

class UserViewsTest(TestCase):
    # Testa se as views de login, registro, perfil e sucesso estão acessíveis e usam os templates corretos
    def test_login_view(self):
        # Obtem a URL da view de login de usuários
        response = self.client.get(reverse('login'))
        # Verifica se a resposta foi bem-sucedida e se o template correto foi usado
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/login.html')

    def test_registration_view(self):
        # Obtem a URL da view de registro de usuários
        response = self.client.get(reverse('registration'))
        # Verifica se a resposta foi bem-sucedida e se o template correto foi usado
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/registration.html')
    
    def test_profile_view_without_login(self):
        # Tenta acessar a view de perfil sem estar autenticado
        response = self.client.get(reverse('profile'))
        # Verifica se a resposta é um redirecionamento para a página de login
        self.assertEqual(response.status_code, 302)

    def test_profile_view_with_login(self):
        # Cria um usuário e faz login
        user_data = {
            'email': 'enzogabriel2@exemplo.com',
            'password': 'senhaForte456',
            'name': 'Enzo Gabriel',
            'gender': 'M',
            'phone': '11999993422',
            'address': 'Av. Teste, 456 - XD',
            'cpf': '11124213344',
        }
        User.objects.create_user(**user_data)
        self.client.login(username='enzogabriel2@exemplo.com', password='senhaForte456')
        # Acessa a view de perfil
        response = self.client.get(reverse('profile'))
        # Verifica se a resposta foi bem-sucedida e se o template correto foi usado
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/profile.html')

    def test_success_view(self):
        # Obtem a URL da view de sucesso
        response = self.client.get(reverse('success'))
        # Verifica se a resposta foi bem-sucedida e se o template correto foi usado
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/success.html')