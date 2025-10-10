from django.test import TestCase
from datetime import date
from django.utils import timezone
from ..forms import ConsultationFilterForm, ConsultationForm
from ..models import Doctor

class ConsultationFormsTest(TestCase):
    def setUp(self):
        # Cria um médico para associar às consultas
        self.doctor_data = {
            'name': 'Dr. João Silva',
            'specialty': 'Cardiologia',
            'gender': 'M',
            'phone': '11987654321',
            'email': 'joaoprofissional@gmail.com',
            'address': 'Rua das Flores, 123 - SP',
            'cpf': '12345678901',
            'date_of_birth': date(1990, 5, 15)
        }
        self.doctor = Doctor.objects.create(**self.doctor_data)
        # Define dados válidos para o formulário de filtro de consultas
        self.form_data = {
            'doctor': self.doctor,
            'date': date(2023, 10, 10),
        }
        self.form = ConsultationFilterForm(data=self.form_data)

    # Testa se o formulário de criação de consultas é válido quando com dados corretos
    def test_creation_form_valid_data(self):
        form_data = {
            'patient_name': 'Maria Oliveira',
            'doctor': self.doctor.id,
            'date': timezone.now().date(),
            'description': 'Consulta de rotina para check-up.',
            'duration': 60,
        }
        form = ConsultationForm(data=form_data)
        # Verifica se o formulário é válido com os dados fornecidos
        self.assertTrue(form.is_valid())

    # Testa se o formulário de criação de consultas é inválido quando com dados incorretos
    def test_creation_form_invalid_data_duration(self):
        form_data = {
            'patient_name': 'Maria Oliveira',
            'doctor': self.doctor,
            'date': timezone.now().date(),
            'description': 'Consulta de rotina para check-up.',
            'duration': 10, # duração inválida
        }
        form = ConsultationForm(data=form_data)
        # Verifica se o formulário é inválido com os dados fornecidos
        self.assertFalse(form.is_valid())
    
    def test_creation_form_invalid_data_patient_name(self):
        form_data = {
            'patient_name': 'a'*101, # nome inválido
            'doctor': self.doctor,
            'date': timezone.now().date(),
            'description': 'Consulta de rotina para check-up.',
            'duration': 60,
        }
        form = ConsultationForm(data=form_data)
        # Verifica se o formulário é inválido com os dados fornecidos
        self.assertFalse(form.is_valid())
        # Verifica se o erro está relacionado ao campo 'patient_name' no formulário
        self.assertIn('patient_name', form.errors)
        # Verifica se o label do campo 'patient_name' está correto
        self.assertEqual(form.fields['patient_name'].label, "Nome do Paciente")

    def test_creation_form_invalid_data_description(self):
        form_data = {
            'patient_name': 'Maria Oliveira',
            'doctor': self.doctor,
            'date': timezone.now().date(),
            'description': 'a'*201, # descrição inválida
            'duration': 60,
        }
        form = ConsultationForm(data=form_data)
        # Verifica se o formulário é inválido com os dados fornecidos
        self.assertFalse(form.is_valid())
        # Verifica se o erro está relacionado ao campo 'description' no formulário
        self.assertIn('description', form.errors)
        # Verifica se o label do campo 'description' está correto
        self.assertEqual(form.fields['description'].label, "")

    def test_creation_form_invalid_data_date(self):
        form_data = {
            'patient_name': 'Maria Oliveira',
            'doctor': self.doctor,
            'date': 'invalid-datetime', # date inválido
            'description': 'Consulta de rotina para check-up.',
            'duration': 60,
        }
        form = ConsultationForm(data=form_data)
        # Verifica se o formulário é inválido com os dados fornecidos
        self.assertFalse(form.is_valid())
        # Verifica se o erro está relacionado ao campo 'date' no formulário
        self.assertIn('date', form.errors)
        # Verifica se o label do campo 'date' está correto
        self.assertEqual(form.fields['date'].label, "Horário")

    def test_creation_form_invalid_data_doctor(self):
        form_data = {
            'patient_name': 'Maria Oliveira',
            'doctor': None, # doctor inválido
            'date': timezone.now().date(),
            'description': 'Consulta de rotina para check-up.',
            'duration': 60,
        }
        form = ConsultationForm(data=form_data)
        # Verifica se o formulário é inválido com os dados fornecidos
        self.assertFalse(form.is_valid())
        # Verifica se o erro está relacionado ao campo 'doctor' no formulário
        self.assertIn('doctor', form.errors)

    # Testa se o formulário de filtro de consultas é válido quando com dados corretos
    def test_filter_form_valid_data(self):
        # Verifica se o formulário é válido com os dados fornecidos
        self.assertTrue(self.form.is_valid())

    # Testa se o formulário de filtro de consultas é inválido quando com dados incorretos
    def test_filter_form_invalid_data_doctor(self):
        # Define dados inválidos para o formulário de filtro de consultas
        form_data = {
            'doctor': None,  # Supondo que não exista um médico com esse ID
            'date': date(2023, 10, 10),
        }
        form = ConsultationFilterForm(data=form_data)
        # Verifica se o formulário é inválido com os dados fornecidos
        self.assertFalse(form.is_valid())
        # Verifica se o erro está relacionado ao campo 'doctor' no formulário
        self.assertIn('doctor', form.errors)
        # Verifica se o label do campo 'doctor' está correto
        self.assertEqual(form.fields['doctor'].label, "Médico")
