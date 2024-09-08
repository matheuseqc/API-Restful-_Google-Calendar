# API Restful com Integração ao Google Calendar

Este projeto é uma API RESTful construída com Django e Django REST Framework. Ela se integra ao Google Calendar para criar e gerenciar eventos.

## Requisitos

- Python 3.8 ou superior
- Pip (gerenciador de pacotes do Python)
- Virtualenv (opcional, para criar ambientes virtuais)
- Conta do Google com acesso ao Google Calendar API

## Configuração do Projeto

### 1. Clonando o Repositório

Clone o repositório para sua máquina local:

```bash
git clone https://github.com/matheuseqc/API-Restful-_Google-Calendar.git
```

```bash
cd API-Restful-_Google-Calendar
```

### 2. Criar e Ativar um Ambiente Virtual

Crie um ambiente virtual para isolar as dependências do projeto:
```bash
python -m venv venv
```
Ative o ambiente virtual:
- Windows
```bash
.\.venv\Scripts\activate 
```

- MAC/LINUX
```bash
source .\.venv\Scripts\activate 
```


### 3.  Instalar as Dependências
Instale as dependências do projeto:
```bash
pip install -r requirements.txt
```

### 4. Configuração das Credenciais do Google Calendar

#### Obter as Credenciais do Google Calendar

1. Vá para o [Google Cloud Console](https://developers.google.com/calendar/api/quickstart/python).
2. Crie um novo projeto ou use um projeto existente.
3. No menu lateral, vá para **APIs & Services** e habilite a **API do Google Calendar**.
4. Navegue até **Credenciais** e clique em **Criar credenciais** para criar um ID de cliente OAuth 2.0.
5. Baixe o arquivo JSON com as credenciais.

#### Configurar as Variáveis de Ambiente

1. Crie um arquivo `.env` na raiz do projeto.
2. Adicione as seguintes variáveis ao arquivo `.env`, com base no arquivo JSON das credenciais baixado:

   ```env
    GOOGLE_CLIENT_ID=<sua-client-id>
    GOOGLE_PROJECT_ID=<seu-project-id>
    GOOGLE_AUTH_URI=<seu-auth-uri>
    GOOGLE_TOKEN_URI=<seu-token-uri>
    GOOGLE_AUTH_PROVIDER_X509_CERT_URL=<seu-auth-provider-cert-url>
    GOOGLE_CLIENT_SECRET=<seu-client-secret>
    GOOGLE_REDIRECT_URIS=http://localhost
  
### 5. Aplicar as Migrações
Antes de executar o servidor, aplique as migrações do banco de dados para configurar as tabelas necessárias:
```bash
python task_manager/manage.py makemigrations
```
```bash
python task_manager/manage.py migrate
```

### 6. Executar o Servidor
```bash
python task_manager/manage.py runserver
```

## Servidor

O servidor estará disponível em [http://localhost:8000/](http://localhost:8000/).

## Estrutura do Projeto

- **api/**: Contém a lógica da API.
  - **api/models.py**: Define os modelos de dados.
  - **api/views.py**: Contém as views e a lógica de negócios.
  - **api/serializers.py**: Define os serializers para a API.
  - **api/filters.py**: Define filtros para a API.
## Testando a API

Você pode testar a API usando ferramentas como Postman ou cURL. Certifique-se de que o servidor está em execução antes de testar os endpoints.

### Exemplo de Requisição com Postman

1. **GET /api/tasks/**: Para obter a lista de tarefas.
   - **Método**: GET
   - **URL**: [http://localhost:8000/api/tasks/](http://localhost:8000/api/tasks/)
   - **Headers**: (Se necessário, adicione cabeçalhos apropriados)
   - **Body**: (Não aplicável para GET)

2. **POST /api/tasks/**: Para criar uma nova tarefa.
   - **Método**: POST
   - **URL**: [http://localhost:8000/api/tasks/](http://localhost:8000/api/tasks/)
   - **Headers**: Content-Type: application/json
   - **Body**: 
     ```json
     {
       "title": "Exemplo de Tarefa",
       "description": "Descrição da tarefa",
       "date": "2024-09-01",
       "time": "12:00:00"
     }
     ```

3. **PUT /api/tasks/{id}/**: Para atualizar uma tarefa existente.
   - **Método**: PUT
   - **URL**: [http://localhost:8000/api/tasks/{id}/](http://localhost:8000/api/tasks/{id}/)
   - **Headers**: Content-Type: application/json
   - **Body**: 
     ```json
     {
       "title": "Tarefa Atualizada",
       "description": "Descrição atualizada",
       "date": "2024-09-02",
       "time": "14:00:00"
     }
     ```

4. **DELETE /api/tasks/{id}/**: Para deletar uma tarefa existente.
   - **Método**: DELETE
   - **URL**: [http://localhost:8000/api/tasks/{id}/](http://localhost:8000/api/tasks/{id}/)
   - **Headers**: (Se necessário, adicione cabeçalhos apropriados)
   - **Body**: (Não aplicável para DELETE)

