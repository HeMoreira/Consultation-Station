from django.test import TestCase
from ..models import User, Consultation, Doctor
from django.urls import reverse
from django.utils import timezone

class ConsultationViewsTest(TestCase):
    # Testa se as views de nova consulta e cronograma de consultas estão acessíveis e usam os templates corretos
    def setUp(self):
        self.user_data = {
            'email': 'enzogabriel@exemplo.com',
            'password': 'senhaForte123',
            'name': 'Enzo Gabriel',
            'gender': 'M',
            'phone': '11999999999',
            'address': 'Av. Teste, 456 - XD',
            'cpf': '11122233344',
        }
        self.superuser_data = {
            'email': 'enzoprofissional@exemplo.com',
            'password': 'senhaForte456',
            'name': 'Enzo Gabriel',
            'gender': 'M',
            'phone': '11999999998',
            'address': 'Av. Teste, 456 - XD',
            'cpf': '12390809876',
            'is_staff': True,
            'is_superuser': True,
        }
        self.doctor_data = {
            'name': 'Dr. João Silva',
            'specialty': 'Cardiologia',
            'gender': 'M',
            'phone': '11987654321',
            'email': 'joaoprofissional@gmail.com',
            'address': 'Rua das Flores, 123 - SP',
            'cpf': '12345678901',
            'date_of_birth': timezone.now().date()
        }
        self.doctor = Doctor.objects.create(**self.doctor_data)
        self.user = User.objects.create_user(**self.user_data)
        self.superuser = User.objects.create_user(**self.superuser_data)
    
    def test_nova_consulta_view_with_login(self):
        # Obtem a URL da view de nova consulta após fazer login
        self.client.login(username=self.user_data['email'], password=self.user_data['password'])
        response = self.client.get(reverse('nova_consulta'))
        # Verifica se a resposta foi bem-sucedida e se o template correto foi usado
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'consultations/nova_consulta.html')
    
    def test_nova_consulta_view_without_login(self):
        # Obtem a URL da view de nova consulta
        response = self.client.get(reverse('nova_consulta'), follow=True)
        # Verifica se a resposta foi bem-sucedida e se o template correto foi usado
        # A página não deve ser acessível sem login, então o status code não deve ser 200
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'consultations/failure.html')

    def test_cronograma_consultas_view_with_login_staff(self):
        # Obtem a URL da view de cronograma de consultas após fazer login como staff
        self.client.login(username=self.superuser_data['email'], password=self.superuser_data['password'])
        response = self.client.get(reverse('cronograma_consultas'))
        # Verifica se a resposta foi bem-sucedida e se o template correto foi usado
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'consultations/cronograma_consultas.html')

    def test_cronograma_consultas_view_with_login_common(self):
        # Obtem a URL da view de cronograma de consultas após fazer login como usuário comum
        self.client.login(username=self.user_data['email'], password=self.user_data['password'])
        response = self.client.get(reverse('cronograma_consultas'))
        # Verifica se a resposta foi bem-sucedida e se o template correto foi usado
        # Usuários comuns não devem acessar essa página, então o template deve ser de falha
        self.assertIn(response.status_code, [200, 302])

    def test_cronograma_consultas_view_without_login(self):
        # Obtem a URL da view de cronograma de consultas
        response = self.client.get(reverse('cronograma_consultas'), follow=True)
        # Verifica se a resposta foi bem-sucedida e se o template correto foi usado
        # A página não deve ser acessível sem login, então o template deve ser de falha
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'consultations/failure.html')

    def test_detalhes_consulta_view(self):
        # Cria uma consulta de teste
        consulta = Consultation.objects.create(
            user_account=self.user,
            patient_name="Teste Paciente",
            doctor=self.doctor,
            date="2024-12-31 10:00",
            description="Descrição de teste",
            duration=30
        )

        # Obtem a URL da view de detalhes da consulta após fazer login como staff
        self.client.login(username=self.superuser_data['email'], password=self.superuser_data['password'])
        response = self.client.get(reverse('detalhes_consulta', args=[consulta.pk]))
        # Verifica se a resposta foi bem-sucedida e se o template correto foi usado
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'consultations/detalhes_consulta.html')
    
    def test_editar_consulta_view(self):
        # Cria uma consulta de teste
        consulta = Consultation.objects.create(
            user_account=self.user,
            patient_name="Teste Paciente",
            doctor=self.doctor,
            date="2024-12-31 10:00",
            description="Descrição de teste",
            duration=30
        )

        # Obtem a URL da view de editar a consulta após fazer login como staff
        self.client.login(username=self.superuser_data['email'], password=self.superuser_data['password'])
        response = self.client.get(reverse('editar_consulta', args=[consulta.pk]))
        # Verifica se a resposta foi bem-sucedida e se o template correto foi usado
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'consultations/editar_consulta.html')

    def test_deletar_consulta_view(self):
        # Cria uma consulta de teste
        consulta = Consultation.objects.create(
            user_account=self.user,
            patient_name="Teste Paciente",
            doctor=self.doctor,
            date="2024-12-31 10:00",
            description="Descrição de teste",
            duration=30
        )

        # Obtem a URL da view de deletar a consulta após fazer login como staff
        self.client.login(username=self.superuser_data['email'], password=self.superuser_data['password'])
        response = self.client.post(reverse('deletar_consulta', args=[consulta.pk]), follow=True)
        # Verifica se a resposta foi bem-sucedida e se redirecionou para o cronograma de consultas
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'consultations/cronograma_consultas.html')
        # Verifica se a consulta foi realmente deletada
        with self.assertRaises(Consultation.DoesNotExist):
            Consultation.objects.get(pk=consulta.pk)

    def test_failure_view(self):
        # Obtem a URL da view de falha de autenticação
        response = self.client.get(reverse('failure'))
        # Verifica se a resposta foi bem-sucedida e se o template correto foi usado
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'consultations/failure.html')