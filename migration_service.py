from google_drive_service import GoogleDriveService
from azure_blob_service import AzureBlobService
from datetime import datetime

class MigrationService:
    def __init__(self):
        self.drive_service = GoogleDriveService()
        self.blob_service = AzureBlobService()
        self.migration_stats = {
            'total': 0,
            'success': 0,
            'failed': 0,
            'skipped': 0
        }
        
    def initialize(self):
        """Inicializa os serviços de Google Drive e Azure Blob"""
        print("\n" + "="*80)
        print("INICIANDO SERVIÇOS DE MIGRAÇÃO")
        print("="*80 + "\n")
        
        if not self.drive_service.authenticate():
            return False
            
        if not self.blob_service.authenticate():
            return False
            
        print("\n✓ Todos os serviços inicializados com sucesso\n")
        return True
    
    def list_source_files(self, folder_id):
        """Lista arquivos da origem (Google Drive)"""
        print("\n" + "="*80)
        print("LISTANDO ARQUIVOS DE ORIGEM (GOOGLE DRIVE)")
        print("="*80 + "\n")
        
        files = self.drive_service.list_files(folder_id)
        self.drive_service.display_files(files)
        return files
    
    def list_destination_files(self):
        """Lista arquivos do destino (Azure Blob Storage)"""
        print("\n" + "="*80)
        print("LISTANDO ARQUIVOS DE DESTINO (AZURE BLOB STORAGE)")
        print("="*80 + "\n")
        
        blobs = self.blob_service.list_blobs()
        self.blob_service.display_blobs(blobs)
        return blobs
    
    def migrate_files(self, folder_id):
        """Realiza a migração dos arquivos do Google Drive para Azure Blob Storage"""
        print("\n" + "="*80)
        print("INICIANDO MIGRAÇÃO DE ARQUIVOS")
        print("="*80 + "\n")
        
        files = self.drive_service.list_files(folder_id)
        
        if not files:
            print("Nenhum arquivo para migrar.")
            return
        
        self.migration_stats['total'] = len(files)
        start_time = datetime.now()
        
        for idx, file in enumerate(files, 1):
            file_name = file['name']
            file_id = file['id']
            
            print(f"\n[{idx}/{len(files)}] Processando: {file_name}")
            print("-" * 80)
            
            # Verifica se é uma pasta do Google Drive
            if file.get('mimeType') == 'application/vnd.google-apps.folder':
                print(f"⊘ Pulando (pasta): {file_name}")
                self.migration_stats['skipped'] += 1
                continue
            
            # Verifica se já existe no Azure
            if self.blob_service.blob_exists(file_name):
                print(f"⊘ Arquivo já existe no destino: {file_name}")
                self.migration_stats['skipped'] += 1
                continue
            
            # Baixa do Google Drive
            print(f"↓ Baixando de Google Drive...")
            file_data = self.drive_service.download_file(file_id, file_name)
            
            if file_data is None:
                print(f"✗ FALHA ao baixar: {file_name}")
                self.migration_stats['failed'] += 1
                continue
            
            # Faz upload para Azure Blob
            print(f"↑ Enviando para Azure Blob Storage...")
            if self.blob_service.upload_blob(file_name, file_data):
                size_mb = len(file_data) / (1024 * 1024)
                print(f"✓ SUCESSO: {file_name} ({size_mb:.2f} MB)")
                self.migration_stats['success'] += 1
            else:
                print(f"✗ FALHA ao enviar: {file_name}")
                self.migration_stats['failed'] += 1
        
        end_time = datetime.now()
        duration = (end_time - start_time).total_seconds()
        
        self.display_migration_summary(duration)
    
    def display_migration_summary(self, duration):
        """Exibe resumo da migração"""
        print("\n" + "="*80)
        print("RESUMO DA MIGRAÇÃO")
        print("="*80)
        print(f"Total de arquivos processados: {self.migration_stats['total']}")
        print(f"✓ Migrados com sucesso: {self.migration_stats['success']}")
        print(f"✗ Falhas: {self.migration_stats['failed']}")
        print(f"⊘ Pulados: {self.migration_stats['skipped']}")
        print(f"Tempo total: {duration:.2f} segundos")
        print("="*80 + "\n")
        
        if self.migration_stats['success'] > 0:
            print("✓ Migração concluída com sucesso!")
        elif self.migration_stats['failed'] > 0:
            print("⚠ Migração concluída com erros.")
        else:
            print("⊘ Nenhum arquivo foi migrado.")