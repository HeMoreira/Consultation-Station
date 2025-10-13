from django.shortcuts import render, redirect
from .forms import CustomRegistrationForm, CustomAuthenticationForm
from django.contrib.auth import login, authenticate
from consultations.models import Consultation
from django.utils import timezone

# View usada para registrar novos usuários
def registrationView(request):
    if request.method == 'POST':
        form = CustomRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('success')
    else:
        form = CustomRegistrationForm()
    return render(request, 'users/registration.html', {'form': form})

# View usada para autenticar usuários existentes
def loginView(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, email=email, password=password)
            # loga o usuário se as credenciais estiverem corretas
            if user is not None:
                login(request, user)
                return redirect('success')
            # esse erro dificilmente será alcançado, pois o formulário já valida as credenciais
            else:
                form.add_error(None, 'Credenciais inválidas. Por favor, tente novamente.')
    else:
        form = CustomAuthenticationForm()
    return render(request, 'users/login.html', {'form': form})

# View para exibir o perfil do usuário logado
def profile(request):
    # Garante que o usuário esteja logado em uma conta
    if not request.user.is_authenticated:
        return redirect('/login')
    # Adiciona as consultas de até dois meses atrás (e posteriores) ao histórico de exibição
    historico_de_consultas = []
    for consulta in Consultation.objects.all():
        if consulta.user_account.cpf == request.user.cpf and consulta.date.month > timezone.now().month - 2 and consulta.date.year >= timezone.now().year:
            historico_de_consultas.append(consulta)

    return render(request, 'users/profile.html', {'historico_de_consultas': historico_de_consultas})

def success(request):
    return render(request, 'users/success.html')