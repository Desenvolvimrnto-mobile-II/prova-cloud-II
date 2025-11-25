import os
from dotenv import load_dotenv

load_dotenv()

# Google Drive Configuration
GOOGLE_CREDENTIALS_PATH = os.getenv('GOOGLE_CREDENTIALS_PATH', 'credentials/google-service-account.json')
GOOGLE_DRIVE_FOLDER_ID = os.getenv('GOOGLE_DRIVE_FOLDER_ID', '1iAZP8hleDw9Y-1cVM7FutE8s34kjjyW1')

# Azure Blob Storage Configuration
AZURE_CONNECTION_STRING = os.getenv('AZURE_CONNECTION_STRING')
AZURE_CONTAINER_NAME = os.getenv('AZURE_CONTAINER_NAME', 'aluno-alessandra')

# Application Settings
SCOPES = ['https://www.googleapis.com/auth/drive.readonly']