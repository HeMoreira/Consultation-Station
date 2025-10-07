from django.test import TestCase
from .models import Consultation, User, Doctor
from django.db import IntegrityError, transaction
from datetime import datetime, date
# Create your tests here.

class ConsultationModelTest(TestCase):

    # Cria uma consulta de exemplo para os testes
    def setUp(self):
        user_data = {
            'email': 'enzogabriel@exemplo.com',
            'password': 'senhaForte456',
            'name': 'Enzo Gabriel',
            'gender': 'M',
            'phone': '11999999999',
            'address': 'Av. Teste, 456 - XD',
            'cpf': '11122233344',
        }
        doctor_data = {
            'name': 'Dr. João Silva',
            'specialty': 'Cardiologia',
            'gender': 'M',
            'phone': '11987654321',
            'email': 'joaoprofissional@gmail.com',
            'address': 'Rua das Flores, 123 - SP',
            'cpf': '12345678901',
            'date_of_birth': date(1990, 5, 15)
        }
        self.consultation_data = {
            'patient_name': 'Ana Clara',
            'date': datetime(2024, 7, 20, 14, 30),
            'description': 'Consulta de rotina',
            'duration': 30,
            'user_account': User.objects.create_user(**user_data),
            'doctor': Doctor.objects.create(**doctor_data),
        }
        self.consultation = Consultation.objects.create(**self.consultation_data)

    # Testa a representação em string da consulta
    def test_str_representation(self):
        self.assertEqual(str(self.consultation), 'Ana Clara - Dr. João Silva')

    # Testa a criação da consulta e seus campos
    def test_doctor_creation_fields(self):
        self.assertEqual(self.consultation.patient_name, self.consultation_data['patient_name'])
        self.assertEqual(self.consultation.date, self.consultation_data['date'])
        self.assertEqual(self.consultation.description, self.consultation_data['description'])
        self.assertEqual(self.consultation.duration, self.consultation_data['duration'])
        self.assertEqual(self.consultation.user_account, self.consultation_data['user_account'])
        self.assertEqual(self.consultation.doctor, self.consultation_data['doctor'])