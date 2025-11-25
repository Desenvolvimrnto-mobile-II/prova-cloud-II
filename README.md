# Migração de Arquivos: Google Drive → Azure Blob Storage

Aplicação desenvolvida para a disciplina de Computação em Nuvem II - FATEC Cotia

## 📋 Descrição

Sistema de migração automatizada de arquivos do Google Drive para Azure Blob Storage, com autenticação segura em ambas plataformas e acompanhamento detalhado do processo de transferência.

## 🎯 Funcionalidades

- ✅ Autenticação segura via Service Account (Google) e Connection String (Azure)
- ✅ Listagem de arquivos de origem (Google Drive)
- ✅ Listagem de arquivos de destino (Azure Blob Storage)
- ✅ Migração completa de arquivos com status em tempo real
- ✅ Tratamento de erros e relatório de migração
- ✅ Verificação de arquivos duplicados (não sobrescreve)
- ✅ Suporte a múltiplos tipos de arquivo

## 📦 Requisitos

- Python 3.8 ou superior
- Conta Google Cloud com Drive API habilitada
- Conta Azure com Blob Storage configurado

## 🚀 Instalação

### 1. Clone ou baixe o repositório
```bash
git clone https://github.com/Desenvolvimrnto-mobile-II/prova-cloud-II.git
cd prova-cloud-II
```

### 2. Crie um ambiente virtual (recomendado)
```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Linux/Mac
source venv/bin/activate
```

### 3. Instale as dependências
```bash
pip install -r requirements.txt
```

### 4. Configure as credenciais

#### Google Drive:
1. Crie a pasta `credentials` na raiz do projeto
2. Salve o arquivo JSON de credenciais como `credentials/google-service-account.json`
3. **IMPORTANTE**: Compartilhe a pasta do Google Drive com o email da Service Account:
   - Email: `drive-to-blob-migration@nuvem-ii-479223.iam.gserviceaccount.com`
   - Permissão: Leitor

#### Azure Blob Storage:
1. Copie o arquivo `.env.example` para `.env`
2. Edite o arquivo `.env` e adicione sua Connection String do Azure
```bash
cp .env.example .env
```

Edite o `.env`:
```bash
AZURE_CONNECTION_STRING=sua_connection_string_aqui
```

## 💻 Uso

### Executar a aplicação
```bash
python main.py
```

### Menu de opções

1. **Listar arquivos de origem (Google Drive)**
   - Exibe todos os arquivos disponíveis na pasta configurada

2. **Listar arquivos de destino (Azure Blob Storage)**
   - Exibe todos os blobs no contêiner do Azure

3. **Realizar migração completa**
   - Migra todos os arquivos do Google Drive para o Azure Blob Storage
   - Exibe status de cada transferência
   - Gera relatório final com estatísticas

4. **Sair**
   - Encerra a aplicação

## 📁 Estrutura do Projeto
```
prova-cloud-II/
│
├── credentials/
│   └── google-service-account.json    # Credenciais Google (não commitar)
│
├── main.py                            # Aplicação principal
├── config.py                          # Configurações
├── google_drive_service.py            # Serviço Google Drive
├── azure_blob_service.py              # Serviço Azure Blob
├── migration_service.py               # Lógica de migração
├── requirements.txt                   # Dependências Python
├── .env.example                       # Exemplo de variáveis de ambiente
├── .gitignore                         # Arquivos ignorados pelo Git
└── README.md                          # Este arquivo
```

## 🔒 Segurança

- ⚠️ **NUNCA** commite o arquivo `google-service-account.json` no Git
- ⚠️ **NUNCA** commite o arquivo `.env` no Git
- ⚠️ Adicione `credentials/` e `.env` no `.gitignore`
- ⚠️ Não compartilhe suas Connection Strings publicamente

## 📊 Exemplo de Saída
```
================================================================================
INICIANDO MIGRAÇÃO DE ARQUIVOS
================================================================================

✓ Total de arquivos encontrados no Google Drive: 5

[1/5] Processando: documento.pdf
--------------------------------------------------------------------------------
↓ Baixando de Google Drive...
↑ Enviando para Azure Blob Storage...
✓ SUCESSO: documento.pdf (2.45 MB)

[2/5] Processando: imagem.jpg
--------------------------------------------------------------------------------
↓ Baixando de Google Drive...
↑ Enviando para Azure Blob Storage...
✓ SUCESSO: imagem.jpg (1.23 MB)

================================================================================
RESUMO DA MIGRAÇÃO
================================================================================
Total de arquivos processados: 5
✓ Migrados com sucesso: 5
✗ Falhas: 0
⊘ Pulados: 0
Tempo total: 12.34 segundos
================================================================================
```

## 🛠️ Tecnologias Utilizadas

- **Python 3.8+**
- **Google Drive API** - Integração com Google Drive
- **Azure SDK for Python** - Integração com Azure Blob Storage
- **google-auth** - Autenticação Google
- **azure-storage-blob** - Manipulação de blobs no Azure

## 👥 Autor

- **Alessandra** - FATEC Cotia
- Disciplina: Computação em Nuvem II
- Professor: Eduardo Tadeu de Almeida

## 📝 Licença

Este projeto foi desenvolvido para fins educacionais.

## 🐛 Problemas Comuns

### Erro de autenticação no Google Drive
- Verifique se o arquivo JSON está no local correto
- Confirme que a pasta foi compartilhada com a Service Account

### Erro de autenticação no Azure
- Verifique se a Connection String está correta no arquivo `.env`
- Confirme que o contêiner existe ou que você tem permissão para criá-lo

### Erro "Nenhum arquivo encontrado"
- Verifique o ID da pasta do Google Drive
- Confirme que a pasta tem arquivos
- Verifique as permissões da Service Account

## 📞 Suporte

Para dúvidas ou problemas, entre em contato com o desenvolvedor.

## 🔗 Links Úteis

- [Repositório GitHub](https://github.com/Desenvolvimrnto-mobile-II/prova-cloud-II)
- [Google Drive API Documentation](https://developers.google.com/drive/api/v3/about-sdk)
- [Azure Blob Storage Documentation](https://docs.microsoft.com/azure/storage/blobs/)
