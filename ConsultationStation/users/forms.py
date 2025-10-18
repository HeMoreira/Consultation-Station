from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import User

#Adiciona campos personalizados ao formulário de criação de usuário
class CustomRegistrationForm(UserCreationForm):
    name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Digite seu Nome Completo', 'size': 35}))
    address = forms.CharField(label="", max_length=255, widget=forms.TextInput(attrs={'placeholder': 'Digite seu Endereço', 'size': 36}))
    date_of_birth = forms.DateField(label='Data de Nascimento', widget=forms.DateInput(attrs={'type': 'date'}))
    email = forms.EmailField(label="Email", max_length=100, widget=forms.EmailInput(attrs={'placeholder': 'Digite seu Email', 'size': 31}))
    password1 = forms.CharField(label="Senha", max_length=100, widget=forms.PasswordInput(attrs={'placeholder': 'Digite sua Senha', 'size': 30}))
    password2 = forms.CharField(label="Senha", max_length=100, widget=forms.PasswordInput(attrs={'placeholder': 'Confirme a sua Senha', 'size': 30}))
    phone = forms.CharField(label="", max_length=15, widget=forms.TextInput(attrs={'placeholder': 'Digite seu Telefone', 'size': 15}))
    cpf = forms.CharField(label="", max_length=11, widget=forms.TextInput(attrs={'placeholder': 'Digite seu CPF', 'size': 15}))
    gender = forms.ChoiceField(label="Gênero", choices=[('M', 'Masculino'), ('F', 'Feminino'), ('O', 'Outro')], widget=forms.Select(attrs={'style': 'width: 215px; height: 20px;'}))

    class Meta:
        model = User
        fields = ('name', 'gender', 'phone', 'email', 'address', 'cpf', 'date_of_birth')

#Faz modificações no formulário de autenticação de usuário
class CustomAuthenticationForm(AuthenticationForm):
    #por mais que utilizemos email para login, os campos devem ser chamados de 'username' e 'password'
    username = forms.EmailField(label="", max_length=100, widget=forms.EmailInput(attrs={'placeholder': 'Digite seu email', 'size': 35}))
    password = forms.CharField(label="", max_length=100, widget=forms.PasswordInput(attrs={'placeholder': 'Digite sua senha', 'size': 35}))
