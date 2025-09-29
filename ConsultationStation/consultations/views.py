from django.shortcuts import render, redirect
from .forms import ConsultationForm, ConsultationFilterForm
from .models import Consultation
from django.utils import timezone

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
    # Garante que o usuário esteja logado em uma conta de staff
    if not request.user.is_authenticated or not request.user.is_staff:
        return redirect('failure')
        
    consultas = Consultation.objects.all()
    horarios = ['08:00','08:30','09:00','09:30','10:00','10:30','11:00','11:30',
                '12:00','12:30','13:00','13:30','14:00','14:30','15:00','15:30',
                '16:00','16:30','17:00','17:30','18:00','18:30','19:00']

    # Chamado após a inserção de Médico e Data no formulário
    if request.method == 'POST':
        form = ConsultationFilterForm(request.POST)
        if form.is_valid():
            # Pega os dados do formulário para envio ao template
            doctor = form.cleaned_data.get('doctor')
            date = form.cleaned_data.get('date')
            medico_atual = doctor.name
            # Considera a data do sistema para a exibição se uma diferente não for colocada
            if date is None:
                date = timezone.now().date()
            # Adiciona os 7 próximos dias a partir da data selecionada para exibição
            lista_datas_exibicao = []
            for i in range(7):
                lista_datas_exibicao.append(date + timezone.timedelta(days=i))

        # Monta a lista de consultas para exibição no template
        listas_consultas = {} # formato {horario: {data: [consultas]}}
        for horario in horarios:
            lista_dias = {}
            for dia in lista_datas_exibicao:
                lista_consultas = []
                for consulta in consultas:
                    # Converte a data da consulta para o timezone local
                    data_consulta = timezone.localtime(consulta.date)
                    # Verifica se a consulta é do médico e dia/horário corretos
                    if data_consulta.strftime("%H:%M") == horario and data_consulta.strftime("%d-%m-%Y") == dia.strftime("%d-%m-%Y") and consulta.doctor.name == medico_atual:
                        lista_consultas.append(consulta)
                        print(data_consulta)
                lista_dias[dia] = lista_consultas
            listas_consultas[horario] = lista_dias
    else:
        form = ConsultationFilterForm()
    return render(request, 'consultations/cronograma_consultas.html', {'listas_consultas': listas_consultas, 'medico_atual': medico_atual, 'lista_datas_exibicao': lista_datas_exibicao, 'form': form})

# View para exibir a página de falha de autenticação
def failure(request):
    return render(request, 'consultations/failure.html')