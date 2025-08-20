# Sistema de Agendamento de Consultas

Sistema web completo para agendamento de consultas. Permite que clientes marquem consultas, enquanto administradores podem gerenciar e visualizar todos os agendamentos.

## Funcionalidades

* **Agendamento por Especialidade:** Clientes podem filtrar médicos por especialidade.
* **Agendamento Dinâmico:** Em menos de um minuto você consegue agendar uma consulta de acordo com as suas preferências.
* **Painel de Administração:** Permite que administradores visualizem, editem e excluam consultas.

## Tecnologias

O projeto foi desenvolvido utilizando as seguintes tecnologias:

* **Backend:**
    * Python 3.1+
    * Django 4.2+
* **Banco de Dados:**
    * SQLite (padrão do Django)
* **Frontend:**
    * HTML5
    * CSS3

#### Instalação
1. Clone o repositório:
    ```bash
    git clone [https://github.com/HeMoreira/Consultation-Station.git](https://github.com/HeMoreira/Consultation-Station.git)
    ```
2. Crie e ative um ambiente virtual:
    ```bash
    python -m venv venv
    source venv/bin/activate  # No Windows: venv\Scripts\activate
    ```
3. Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```

#### Configuração e Migração
1. Execute as migrações para criar o banco de dados:
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```
2. Crie um superusuário para acessar o painel de administração:
    ```bash
    python manage.py createsuperuser
    ```

#### Execução
1. Inicie o servidor de desenvolvimento:
    ```bash
    python manage.py runserver
    ```
2. Acesse o projeto em seu navegador:
    - Página principal: `http://127.0.0.1:8000/`
    - Painel de Administração: `http://127.0.0.1:8000/admin/`