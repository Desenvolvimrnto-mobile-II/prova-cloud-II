from azure.storage.blob import BlobServiceClient, ContainerClient
from azure.core.exceptions import ResourceExistsError, ResourceNotFoundError
import config

class AzureBlobService:
    def __init__(self):
        self.blob_service_client = None
        self.container_client = None
        
    def authenticate(self):
        """Autentica no Azure Blob Storage usando Connection String"""
        try:
            self.blob_service_client = BlobServiceClient.from_connection_string(
                config.AZURE_CONNECTION_STRING
            )
            
            # Verifica se o contêiner existe, senão cria
            try:
                self.container_client = self.blob_service_client.get_container_client(
                    config.AZURE_CONTAINER_NAME
                )
                self.container_client.get_container_properties()
                print(f"✓ Contêiner '{config.AZURE_CONTAINER_NAME}' encontrado")
            except ResourceNotFoundError:
                self.container_client = self.blob_service_client.create_container(
                    config.AZURE_CONTAINER_NAME
                )
                print(f"✓ Contêiner '{config.AZURE_CONTAINER_NAME}' criado com sucesso")
            
            print("✓ Autenticação no Azure Blob Storage realizada com sucesso")
            return True
        except Exception as e:
            print(f"✗ Erro ao autenticar no Azure Blob Storage: {str(e)}")
            return False
    
    def upload_blob(self, blob_name, data):
        """Faz upload de um blob para o Azure Blob Storage"""
        try:
            blob_client = self.container_client.get_blob_client(blob_name)
            blob_client.upload_blob(data, overwrite=True)
            return True
        except Exception as e:
            print(f"✗ Erro ao fazer upload do blob '{blob_name}': {str(e)}")
            return False
    
    def list_blobs(self):
        """Lista todos os blobs do contêiner"""
        try:
            blobs = list(self.container_client.list_blobs())
            print(f"✓ Total de blobs encontrados no Azure Blob Storage: {len(blobs)}")
            return blobs
        except Exception as e:
            print(f"✗ Erro ao listar blobs do Azure Blob Storage: {str(e)}")
            return []
    
    def display_blobs(self, blobs):
        """Exibe lista de blobs formatada"""
        if not blobs:
            print("Nenhum blob encontrado.")
            return
        
        print("\n" + "="*80)
        print("BLOBS NO AZURE BLOB STORAGE")
        print("="*80)
        for idx, blob in enumerate(blobs, 1):
            size_mb = blob.size / (1024 * 1024)
            print(f"{idx}. {blob.name}")
            print(f"   Tamanho: {size_mb:.2f} MB")
            print(f"   Última modificação: {blob.last_modified}")
            print(f"   Content Type: {blob.content_settings.content_type if blob.content_settings else 'N/A'}")
            print("-" * 80)
        print()
    
    def blob_exists(self, blob_name):
        """Verifica se um blob já existe no contêiner"""
        try:
            blob_client = self.container_client.get_blob_client(blob_name)
            blob_client.get_blob_properties()
            return True
        except ResourceNotFoundError:
            return False
        except Exception:
            return False