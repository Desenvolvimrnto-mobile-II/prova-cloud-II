#!/usr/bin/env python3
"""
Script de Migração de Arquivos
Google Drive -> Azure Blob Storage

Desenvolvido para: FATEC Cotia - Computação em Nuvem II
Autor: Alessandra
Data: 24/11/2025
"""

from migration_service import MigrationService
import config
import sys

def print_header():
    """Exibe cabeçalho da aplicação"""
    print("\n" + "="*80)
    print(" " * 15 + "MIGRAÇÃO DE ARQUIVOS: GOOGLE DRIVE → AZURE BLOB")
    print("="*80)
    print("Origem: Google Drive")
    print(f"Pasta ID: {config.GOOGLE_DRIVE_FOLDER_ID}")
    print(f"\nDestino: Azure Blob Storage")
    print(f"Contêiner: {config.AZURE_CONTAINER_NAME}")
    print("="*80 + "\n")

def print_menu():
    """Exibe menu de opções"""
    print("\n" + "="*80)
    print("MENU DE OPÇÕES")
    print("="*80)
    print("1. Listar arquivos de origem (Google Drive)")
    print("2. Listar arquivos de destino (Azure Blob Storage)")
    print("3. Realizar migração completa")
    print("4. Sair")
    print("="*80)

def main():
    """Função principal da aplicação"""
    print_header()
    
    # Inicializa o serviço de migração
    migration = MigrationService()
    
    if not migration.initialize():
        print("\n✗ Erro ao inicializar os serviços. Verifique as credenciais e tente novamente.")
        sys.exit(1)
    
    while True:
        print_menu()
        choice = input("\nEscolha uma opção (1-4): ").strip()
        
        if choice == '1':
            # Listar arquivos do Google Drive
            migration.list_source_files(config.GOOGLE_DRIVE_FOLDER_ID)
            
        elif choice == '2':
            # Listar blobs do Azure Blob Storage
            migration.list_destination_files()
            
        elif choice == '3':
            # Realizar migração
            confirm = input("\nDeseja iniciar a migração dos arquivos? (s/n): ").strip().lower()
            if confirm == 's':
                migration.migrate_files(config.GOOGLE_DRIVE_FOLDER_ID)
                
                # Exibe arquivos no destino após migração
                print("\nVerificando arquivos no destino...")
                migration.list_destination_files()
            else:
                print("Migração cancelada.")
                
        elif choice == '4':
            print("\n✓ Encerrando aplicação. Até logo!")
            sys.exit(0)
            
        else:
            print("\n✗ Opção inválida. Tente novamente.")
        
        input("\nPressione ENTER para continuar...")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n✗ Aplicação interrompida pelo usuário.")
        sys.exit(0)
    except Exception as e:
        print(f"\n✗ Erro inesperado: {str(e)}")
        sys.exit(1)