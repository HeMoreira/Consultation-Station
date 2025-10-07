from django.test import TestCase
from .models import Doctor
from django.db import IntegrityError, transaction
from datetime import date
# Create your tests here.

class DoctorModelTest(TestCase):
    # Cria um médico de exemplo para os testes
    def setUp(self):
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
    
    # Testa a representação em string do médico (Especialidade - Nome)
    def test_str_representation(self):
        self.assertEqual(str(self.doctor), 'Cardiologia - Dr. João Silva')

    # Testa a criação do médico e seus campos
    def test_doctor_creation_fields(self):
        self.assertEqual(self.doctor.name, self.doctor_data['name'])
        self.assertEqual(self.doctor.specialty, self.doctor_data['specialty'])
        self.assertEqual(self.doctor.gender, self.doctor_data['gender'])
        self.assertEqual(self.doctor.phone, self.doctor_data['phone'])
        self.assertEqual(self.doctor.email, self.doctor_data['email'])
        self.assertEqual(self.doctor.address, self.doctor_data['address'])
        self.assertEqual(self.doctor.cpf, self.doctor_data['cpf'])

    # Garante que o CPF e o Email são únicos
    def test_unique_cpf_constraint(self):
        with transaction.atomic():
            with self.assertRaises(IntegrityError):
                Doctor.objects.create(
                    name='Dra. Maria Souza',
                    specialty='Dermatologia',
                    gender='F',
                    phone='11912345678',
                    email='mariadesouza@gmail.com',
                    address='Av. Central, 456 - RJ',
                    cpf='12345678901',  # CPF duplicado
                )
        
        with transaction.atomic():
            with self.assertRaises(IntegrityError):
                Doctor.objects.create(
                    name='Dra. Maria Souza',
                    specialty='Dermatologia',
                    gender='F',
                    phone='11912345678',
                    email='joaoprofissional@gmail.com',  # Email duplicado
                    address='Av. Central, 456 - RJ',
                    cpf='10987654321',
                )