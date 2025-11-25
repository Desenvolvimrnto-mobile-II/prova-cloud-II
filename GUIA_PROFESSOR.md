# 🎓 GUIA PARA O PROFESSOR - Executar Aplicação Localmente

## 📋 Pré-requisitos

- Python 3.8 ou superior instalado
- Git instalado (para clonar o repositório)
- Conexão com a internet

## 🚀 Passo a Passo para Execução

### 1️⃣ Clonar o Repositório
```bash
git clone https://github.com/Desenvolvimrnto-mobile-II/prova-cloud-II.git
cd prova-cloud-II
```

### 2️⃣ Criar Ambiente Virtual (Recomendado)

**Windows (PowerShell):**
```powershell
python -m venv venv
venv\Scripts\activate
```

**Windows (CMD):**
```cmd
python -m venv venv
venv\Scripts\activate.bat
```

**Linux/Mac:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3️⃣ Instalar Dependências
```bash
pip install -r requirements.txt
```

### 4️⃣ Configurar Credenciais

#### A) Criar pasta de credenciais
```bash
mkdir credentials
```

#### B) Adicionar arquivo JSON do Google Drive

Crie o arquivo `credentials/google-service-account.json` com o seguinte conteúdo:
```json
{
  "type": "service_account",
  "project_id": "nuvem-ii-479223",
  "private_key_id": "e30c8044da6362f230a3aa40a98d430166747160",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQC49yn8UbG30uwW\na9KyHndjM6i0+zyjXvBnxDCul49jJi1z6bgX5bfDpX/ODR0Mtir7vVLemG3DMN+O\n/K59NolsDHiclSkH2Ehu7q7qaLRJ6Zfk/qQ9Moay5yW7zpiqhVh0k/KKcmEE1BZZ\nYqRfBO54ewJUW8nQOTNmEJ/fEPWu+HhPYmY5ABlXS+FtWw+oQ5poqOgM2P3tFq3Y\n5X8Am/0C82XNlcAxbAmyByZeAPXSZJizim+cgcxQ/K5Vxp9ehvKoqrwcvZ1f9Wmn\nUz3h7iQEZVXgnHUnXlp4jOQjb4itLk7WZoSzYGiUjOa5zI5SEv0ICu5yconfx3qN\ng1p0H73DAgMBAAECggEAGi1IsN/y8dwU83tg/zpWlSCLgMmJpGlcRqM6bIsgjNyr\nVBtApYkqP7MdalDqypDBdo0tvDkAV76D9R2HqEremf8N1sM5YlXWsnRvJteYpFk9\n2Pe80Lhk3c7exTyQ2Jk0kpMZoURcvK0zWIUgVB5DjaODCeNPpXti7c/ugEhLLO7Z\nl+cvJU1pSAzDXgvvsKVA5329OkB1qxsq/6I5lptxyG1VVZPUEJoE5YMfzNUgG/eB\natARITqwnwcWUvwTi7jPPIUsKm5BepmpNRUpMjNAApXI258fU+0/NPmu2nln/Z25\nm47qQYnRua1M2NQH71QmqfBD5qAGYVVk7Lp+rcDaaQKBgQDjwhpf3tmB8m/qlFCX\nPXi8B7pPF1nYP8DLvweSSSmxFHqXKPCDQ3vf8OAqI46323ZtC22fqhHFCOCqbWMg\nLAPCB0hfh1u0+NkO+5SpTrwuWJRSHxtn/q9cJJNBLv6ZRN5UcsVr6l6k32rKf3Dg\nXT67Thml2QhhJmIpmNMUAaiCNwKBgQDP5qjnO3h3uQqSKhG8mnYJDpSK/josnfBH\n3yc6HVlHfcYDlaBAiIeKkH2zAPudPa67j1dM8bKGCJt+s/aRgJ0byFFsWs0j+Enf\nqPJTH3OW1qGjlR9DHh/EjYbD/S77vpnqSjjMJu5oql49EdfV8L3ma2RNPUG5Lahh\nNZ9RHzTK1QKBgG4nxfvSW56m9Awfua68U3WVwz1XjOOzSfsBJJdS/XAg+H29lj3W\nWMZhyPl4gyFXarqoyVdsuPV0Kr0i9Mttnk+smAtj+y3XIZxGf4s3gnpj6zCgzO+K\nVaQaKIJhSVA159YuQF/GVgol6I+R/bT2RE3xIyR8iLn8B4QY3xYRC0AXAoGALEQO\nfn15HvS1PX3bnO6+ZxtFoXqT5GAUgxkOfx80nTY4bRb0sgjf4y70tKJm8InrpF/W\n1Lk5q7Q1d3rV6xEZYor6WznSJ/B7ujV8sxolQF6et/fOWjoVxYHkyeIkmNFycCIx\nibZYWMy9l/8ul4zUwjTnfFKopccE7P2/2EPut6kCgYEAwp7bvTLTqoZgm29f4TaN\nlriJmhRK9Z1kyHxsCn0GayxdRM+aGRxOkI3ojClcruZMXlNS2f7zXVQhxdgwPfbY\ndThmugrXeFUk8aYkkSYrbRdM2bRVdQl0/HY8eILsGxuVd6fERB6mdbW9VqHG/DUs\nIrsyraN3PM9wJ+fi6UM/oBY=\n-----END PRIVATE KEY-----\n",
  "client_email": "drive-to-blob-migration@nuvem-ii-479223.iam.gserviceaccount.com",
  "client_id": "106245355891406137008",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/drive-to-blob-migration%40nuvem-ii-479223.iam.gserviceaccount.com",
  "universe_domain": "googleapis.com"
}
```

#### C) Criar arquivo .env com credenciais do Azure

Crie o arquivo `.env` na raiz do projeto com o seguinte conteúdo:
```bash
# Google Drive Configuration
GOOGLE_CREDENTIALS_PATH=credentials/google-service-account.json
GOOGLE_DRIVE_FOLDER_ID=1iAZP8hleDw9Y-1cVM7FutE8s34kjjyW1

# Azure Blob Storage Configuration
AZURE_CONNECTION_STRING=DefaultEndpointsProtocol=https;AccountName=stop2cn2;AccountKey=3EDW9QC8Y97sGwWvIdUcPspX9MmPJ1hIbB97GSsOzWomiEbfq7TznWrqmwW83F3YXSOBD5owcumC+ASt61xRrQ==;EndpointSuffix=core.windows.net
AZURE_CONTAINER_NAME=aluno-alessandra
```

### 5️⃣ ⚠️ IMPORTANTE: Compartilhar Pasta do Google Drive

**Antes de executar a aplicação**, é necessário compartilhar a pasta do Google Drive com a Service Account:

1. Acesse a pasta: https://drive.google.com/drive/folders/1iAZP8hleDw9Y-1cVM7FutE8s34kjjyW1
2. Clique no botão **"Compartilhar"** ou no ícone de compartilhamento
3. Adicione o seguinte email: `drive-to-blob-migration@nuvem-ii-479223.iam.gserviceaccount.com`
4. Selecione a permissão: **"Leitor"**
5. Desmarque a opção "Notificar pessoas" (opcional)
6. Clique em **"Compartilhar"**

**⚠️ Sem este passo, a aplicação não conseguirá acessar os arquivos do Google Drive!**

### 6️⃣ Executar a Aplicação
```bash
python main.py
```

## 📱 Usando a Aplicação

Ao executar, você verá um menu com 4 opções:
```
================================================================================
MENU DE OPÇÕES
================================================================================
1. Listar arquivos de origem (Google Drive)
2. Listar arquivos de destino (Azure Blob Storage)
3. Realizar migração completa
4. Sair
================================================================================
```

### Opção 1: Listar arquivos de origem
- Exibe todos os arquivos disponíveis na pasta do Google Drive
- Mostra: nome, ID, tipo MIME e tamanho

### Opção 2: Listar arquivos de destino
- Exibe todos os blobs no contêiner do Azure Blob Storage
- Mostra: nome, tamanho, data de modificação e tipo de conteúdo

### Opção 3: Realizar migração completa
- Transfere todos os arquivos do Google Drive para o Azure Blob Storage
- Exibe status de cada transferência (sucesso/erro)
- Pula arquivos duplicados automaticamente
- Gera relatório final com estatísticas

### Opção 4: Sair
- Encerra a aplicação

## 📊 Exemplo de Execução Completa
```
================================================================================
              MIGRAÇÃO DE ARQUIVOS: GOOGLE DRIVE → AZURE BLOB
================================================================================
Origem: Google Drive
Pasta ID: 1iAZP8hleDw9Y-1cVM7FutE8s34kjjyW1

Destino: Azure Blob Storage
Contêiner: aluno-alessandra
================================================================================

================================================================================
INICIANDO SERVIÇOS DE MIGRAÇÃO
================================================================================

✓ Autenticação no Google Drive realizada com sucesso
✓ Contêiner 'aluno-alessandra' encontrado
✓ Autenticação no Azure Blob Storage realizada com sucesso

✓ Todos os serviços inicializados com sucesso

================================================================================
MENU DE OPÇÕES
================================================================================
1. Listar arquivos de origem (Google Drive)
2. Listar arquivos de destino (Azure Blob Storage)
3. Realizar migração completa
4. Sair
================================================================================

Escolha uma opção (1-4): 3

Deseja iniciar a migração dos arquivos? (s/n): s

================================================================================
INICIANDO MIGRAÇÃO DE ARQUIVOS
================================================================================

✓ Total de arquivos encontrados no Google Drive: 3

[1/3] Processando: documento.pdf
--------------------------------------------------------------------------------
↓ Baixando de Google Drive...
↑ Enviando para Azure Blob Storage...
✓ SUCESSO: documento.pdf (2.45 MB)

[2/3] Processando: planilha.xlsx
--------------------------------------------------------------------------------
↓ Baixando de Google Drive...
↑ Enviando para Azure Blob Storage...
✓ SUCESSO: planilha.xlsx (0.85 MB)

[3/3] Processando: apresentacao.pptx
--------------------------------------------------------------------------------
↓ Baixando de Google Drive...
↑ Enviando para Azure Blob Storage...
✓ SUCESSO: apresentacao.pptx (5.23 MB)

================================================================================
RESUMO DA MIGRAÇÃO
================================================================================
Total de arquivos processados: 3
✓ Migrados com sucesso: 3
✗ Falhas: 0
⊘ Pulados: 0
Tempo total: 8.45 segundos
================================================================================

✓ Migração concluída com sucesso!
```

## 🐛 Possíveis Problemas e Soluções

### ❌ Erro: "Arquivo de credenciais não encontrado"
**Solução:** Verifique se o arquivo `credentials/google-service-account.json` existe e está no local correto.

### ❌ Erro: "403 Forbidden" ao acessar Google Drive
**Solução:** A pasta do Google Drive não foi compartilhada com a Service Account. Siga o passo 5️⃣.

### ❌ Erro: "No module named 'google'"
**Solução:** As dependências não foram instaladas. Execute: `pip install -r requirements.txt`

### ❌ Erro de autenticação no Azure
**Solução:** Verifique se o arquivo `.env` foi criado corretamente com a Connection String.

### ❌ Erro: "Nenhum arquivo encontrado"
**Solução:** 
- Verifique se o ID da pasta está correto no arquivo `.env`
- Confirme que a pasta tem arquivos
- Verifique se a Service Account tem permissão de leitura na pasta

## 📦 Estrutura de Arquivos Esperada

Após configurar, a estrutura deve estar assim:
```
prova-cloud-II/
├── credentials/
│   └── google-service-account.json  ← Você criou este arquivo
├── venv/                             ← Ambiente virtual (criado automaticamente)
├── .env                              ← Você criou este arquivo
├── .env.example
├── .gitignore
├── README.md
├── main.py
├── config.py
├── google_drive_service.py
├── azure_blob_service.py
├── migration_service.py
└── requirements.txt
```

## ✅ Checklist de Verificação

Antes de executar, confirme:

- [ ] Python 3.8+ instalado
- [ ] Repositório clonado
- [ ] Ambiente virtual criado e ativado
- [ ] Dependências instaladas (`pip install -r requirements.txt`)
- [ ] Pasta `credentials/` criada
- [ ] Arquivo `google-service-account.json` criado e salvo
- [ ] Arquivo `.env` criado com as credenciais do Azure
- [ ] Pasta do Google Drive compartilhada com a Service Account
- [ ] Conexão com internet ativa

## 🎓 Informações Adicionais

- **Tempo estimado de configuração:** 5-10 minutos
- **Tempo de execução da migração:** Varia conforme o tamanho e quantidade dos arquivos
- **Credenciais fornecidas:** Válidas até 25/12/2025 (conforme SAS URL do Azure)

## 📞 Suporte

Em caso de dúvidas durante a execução:
- Verifique os logs de erro exibidos no console
- Consulte a seção "Possíveis Problemas e Soluções"
- Todos os arquivos de código contêm tratamento de erros detalhado

---

**Desenvolvido por:** Alessandra - FATEC Cotia  
**Disciplina:** Computação em Nuvem II  
**Professor:** Eduardo Tadeu de Almeida  
**Data:** 24/11/2025
