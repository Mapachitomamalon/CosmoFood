#!/usr/bin/env python
"""
Script para generar configuración segura de Django

Uso:
    python setup_security.py
"""

import os
import secrets
from pathlib import Path

def generate_secret_key(length=50):
    """Genera una SECRET_KEY segura"""
    return ''.join(secrets.choice('abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)') for _ in range(length))

def create_env_file():
    """Crea archivo .env con valores seguros"""
    base_dir = Path(__file__).parent
    env_file = base_dir / '.env'
    
    if env_file.exists():
        response = input(f"{env_file} ya existe. ¿Sobrescribir? (s/n): ")
        if response.lower() != 's':
            print("Operación cancelada.")
            return
    
    # Generar secret key segura
    secret_key = generate_secret_key()
    
    # Pedir datos al usuario
    print("\n" + "="*50)
    print("CONFIGURACIÓN DE SEGURIDAD DE COSMOFOOD")
    print("="*50 + "\n")
    
    debug = input("¿Modo DEBUG? (s/n, default=n): ").lower() == 's'
    allowed_hosts = input("Hosts permitidos (ej: 3.147.189.150,dominio.com): ").strip()
    
    if not allowed_hosts:
        allowed_hosts = "localhost,127.0.0.1"
    
    # Configurar HTTPS solo si no es debug
    if debug:
        secure_ssl = False
        session_cookie_secure = False
        csrf_cookie_secure = False
    else:
        secure_ssl = input("¿Usar HTTPS (SECURE_SSL_REDIRECT)? (s/n, default=s): ").lower() != 'n'
        session_cookie_secure = secure_ssl
        csrf_cookie_secure = secure_ssl
    
    # Base de datos
    use_postgres = input("¿Usar PostgreSQL en producción? (s/n, default=n): ").lower() == 's'
    
    # Construir contenido del .env
    env_content = f"""# Configuración de CosmoFood
# GENERADO AUTOMÁTICAMENTE - NO COMPARTIR ESTE ARCHIVO

# Django Configuration
DEBUG={str(debug).lower()}
SECRET_KEY={secret_key}
ALLOWED_HOSTS={allowed_hosts}

# Security Configuration
SECURE_SSL_REDIRECT={str(secure_ssl).lower()}
SESSION_COOKIE_SECURE={str(session_cookie_secure).lower()}
CSRF_COOKIE_SECURE={str(csrf_cookie_secure).lower()}
SECURE_HSTS_SECONDS=31536000
SECURE_HSTS_INCLUDE_SUBDOMAINS=true
SECURE_HSTS_PRELOAD=true

# CSRF
CSRF_TRUSTED_ORIGINS=https://{allowed_hosts.replace(',', ',https://')}

# Database Configuration
"""

    if use_postgres:
        db_name = input("Nombre de base de datos: ").strip() or "cosmofood_db"
        db_user = input("Usuario de BD: ").strip() or "cosmofood"
        db_password = input("Contraseña de BD (dejar vacío para generar): ").strip()
        db_host = input("Host de BD (default=localhost): ").strip() or "localhost"
        db_port = input("Puerto de BD (default=5432): ").strip() or "5432"
        
        if not db_password:
            db_password = secrets.token_urlsafe(16)
        
        env_content += f"""DB_ENGINE=django.db.backends.postgresql
DB_NAME={db_name}
DB_USER={db_user}
DB_PASSWORD={db_password}
DB_HOST={db_host}
DB_PORT={db_port}
"""
    else:
        env_content += "DB_ENGINE=django.db.backends.sqlite3\n"
    
    # Email Configuration (opcional)
    setup_email = input("\n¿Configurar Email SMTP? (s/n, default=n): ").lower() == 's'
    
    if setup_email:
        email_host = input("Host SMTP (ej: smtp.gmail.com): ").strip()
        email_port = input("Puerto SMTP (ej: 587): ").strip()
        email_use_ssl = input("¿Usar SSL? (s/n): ").lower() == 's'
        email_user = input("Email: ").strip()
        email_password = input("Contraseña app: ").strip()
        
        env_content += f"""
# Email Configuration
EMAIL_HOST={email_host}
EMAIL_PORT={email_port}
EMAIL_USE_SSL={str(email_use_ssl).lower()}
EMAIL_HOST_USER={email_user}
EMAIL_HOST_PASSWORD={email_password}
DEFAULT_FROM_EMAIL={email_user}
"""
    
    # Guardar archivo
    env_file.write_text(env_content)
    
    print("\n" + "="*50)
    print("✅ Archivo .env creado exitosamente!")
    print("="*50)
    print(f"\nUbicación: {env_file}")
    print(f"SECRET_KEY: {secret_key}")
    
    if use_postgres and 'db_password' in locals():
        print(f"DB_PASSWORD: {db_password}")
    
    print("\n⚠️  IMPORTANTE: No compartir este archivo!")
    print("   Agregarlo a .gitignore (ya está incluido)")

if __name__ == '__main__':
    create_env_file()
