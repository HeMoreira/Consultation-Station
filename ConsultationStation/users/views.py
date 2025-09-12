from django.shortcuts import render, redirect
from .forms import CustomRegistrationForm, CustomAuthenticationForm
from django.contrib.auth import login, authenticate

#View usada para registrar novos usuários
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
            if user is not None:
                login(request, user)
                return redirect('success')
            else:
                form.add_error(None, 'Credenciais inválidas. Por favor, tente novamente.')
    else:
        form = CustomAuthenticationForm()
    return render(request, 'users/login.html', {'form': form})

def success(request):
    return render(request, 'users/success.html')