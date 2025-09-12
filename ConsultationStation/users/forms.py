from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import User

#Adiciona campos personalizados ao formulário de criação de usuário
class CustomRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('name', 'gender', 'phone', 'email', 'address', 'cpf', 'date_of_birth')

#Faz modificações no formulário de autenticação de usuário
class CustomAuthenticationForm(AuthenticationForm):
    #por mais que utilizemos email para login, os campos devem ser chamados de 'username' e 'password'
    username = forms.EmailField(label='Email')
    password = forms.CharField(label='Senha', widget=forms.PasswordInput)
