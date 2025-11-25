from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseDownload
import io
import config

class GoogleDriveService:
    def __init__(self):
        self.credentials = None
        self.service = None
        
    def authenticate(self):
        """Autentica no Google Drive usando Service Account"""
        try:
            self.credentials = service_account.Credentials.from_service_account_file(
                config.GOOGLE_CREDENTIALS_PATH,
                scopes=config.SCOPES
            )
            self.service = build('drive', 'v3', credentials=self.credentials)
            print("✓ Autenticação no Google Drive realizada com sucesso")
            return True
        except FileNotFoundError:
            print(f"✗ Erro: Arquivo de credenciais não encontrado em {config.GOOGLE_CREDENTIALS_PATH}")
            return False
        except Exception as e:
            print(f"✗ Erro ao autenticar no Google Drive: {str(e)}")
            return False
    
    def list_files(self, folder_id):
        """Lista todos os arquivos de uma pasta do Google Drive"""
        try:
            files = []
            page_token = None
            
            while True:
                query = f"'{folder_id}' in parents and trashed=false"
                response = self.service.files().list(
                    q=query,
                    spaces='drive',
                    fields='nextPageToken, files(id, name, mimeType, size)',
                    pageToken=page_token
                ).execute()
                
                files.extend(response.get('files', []))
                page_token = response.get('nextPageToken', None)
                
                if page_token is None:
                    break
            
            print(f"✓ Total de arquivos encontrados no Google Drive: {len(files)}")
            return files
        except Exception as e:
            print(f"✗ Erro ao listar arquivos do Google Drive: {str(e)}")
            return []
    
    def download_file(self, file_id, file_name):
        """Baixa um arquivo do Google Drive e retorna como bytes"""
        try:
            request = self.service.files().get_media(fileId=file_id)
            file_buffer = io.BytesIO()
            downloader = MediaIoBaseDownload(file_buffer, request)
            
            done = False
            while not done:
                status, done = downloader.next_chunk()
            
            file_buffer.seek(0)
            return file_buffer.getvalue()
        except Exception as e:
            print(f"✗ Erro ao baixar arquivo '{file_name}': {str(e)}")
            return None
    
    def display_files(self, files):
        """Exibe lista de arquivos formatada"""
        if not files:
            print("Nenhum arquivo encontrado.")
            return
        
        print("\n" + "="*80)
        print("ARQUIVOS NO GOOGLE DRIVE")
        print("="*80)
        for idx, file in enumerate(files, 1):
            size = int(file.get('size', 0)) if file.get('size') else 0
            size_mb = size / (1024 * 1024)
            print(f"{idx}. {file['name']}")
            print(f"   ID: {file['id']}")
            print(f"   Tipo: {file.get('mimeType', 'N/A')}")
            print(f"   Tamanho: {size_mb:.2f} MB")
            print("-" * 80)
        print()