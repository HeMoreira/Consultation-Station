from django.test import TestCase
from django.urls import reverse

class UserViewsTest(TestCase):
    # Testa se as views de login, registro e sucesso estão acessíveis e usam os templates corretos
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
    
    def test_success_view(self):
        # Obtem a URL da view de sucesso
        response = self.client.get(reverse('success'))
        # Verifica se a resposta foi bem-sucedida e se o template correto foi usado
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/success.html')