from django.shortcuts import render, redirect
from .forms import ConsultationForm

# View para criar uma nova consulta
def nova_consulta(request):
    # Garante que o usuário esteja logado em uma conta
    if not request.user.is_authenticated:
        return redirect('failure')
    # Valida e salva o formulário de nova consulta
    if request.method == 'POST':
        form = ConsultationForm(request.POST)
        if form.is_valid():
            consulta = form.save(commit=False)
            consulta.user_account = request.user
            consulta.save()
            return redirect('success')
    else:
        form = ConsultationForm()
    return render(request, 'consultations/nova_consulta.html', {'form': form})

# View para exibição das consultas agendadas de forma organizada
def cronograma_consultas(request):
    return render(request, 'consultations/cronograma_consultas.html')

# View para exibir a página de falha de autenticação
def failure(request):
    return render(request, 'consultations/failure.html')