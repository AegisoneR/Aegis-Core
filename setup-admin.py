#!/usr/bin/env python3
"""
Admin Setup Script for AEGIS Motors

This script helps you set up admin credentials for the dashboard.

Usage:
    python setup-admin.py
    
This will generate an admin username and password and print instructions.

For production, set the ADMIN_PASSWORD environment variable:
    export ADMIN_PASSWORD="your-secure-password"
    python server.py
"""

import secrets
import hashlib
import os


def generate_credentials():
    """Generate secure admin credentials"""
    username = "admin"
    password = secrets.token_urlsafe(16)  # 16 bytes = ~22 char token
    
    return {
        "username": username,
        "password": password,
        "password_hash": hashlib.sha256(password.encode()).hexdigest()
    }


def print_setup_instructions(creds):
    """Print setup instructions"""
    print("=" * 60)
    print("AEGIS ONE - ADMIN CREDENTIALS")
    print("=" * 60)
    print()
    print("IMPORTANT: Save these credentials securely!")
    print()
    print(f"Username: {creds['username']}")
    print(f"Password: {creds['password']}")
    print()
    print("-" * 60)
    print("OPTION 1: Environment Variable (Recommended)")
    print("-" * 60)
    print()
    print("# Linux/Mac:")
    print(f"export ADMIN_PASSWORD='{creds['password']}'")
    print("python server.py")
    print()
    print("# Windows (Command Prompt):")
    print(f'set ADMIN_PASSWORD={creds["password"]}')
    print("python server.py")
    print()
    print("# Windows (PowerShell):")
    print(f'$env:ADMIN_PASSWORD="{creds["password"]}"')
    print("python server.py")
    print()
    print("-" * 60)
    print("OPTION 2: One-time Setup")
    print("-" * 60)
    print()
    print(f"# Run once to print credentials:")
    print("python setup-admin.py")
    print()
    print(f"# Then set password manually:")
    print(f"export ADMIN_PASSWORD='{creds['password']}'")
    print("python server.py")
    print()
    print("-" * 60)
    print("SECURITY NOTES")
    print("-" * 60)
    print()
    print("- Use a strong, unique password")
    print("- Don't share credentials via email or chat")
    print("- Rotate passwords periodically")
    print("- Use HTTPS in production")
    print("- Store password hash securely if modifying server.py")
    print()
    print("=" * 60)


def verify_password(password, password_hash):
    """Verify a password against its hash"""
    return hashlib.sha256(password.encode()).hexdigest() == password_hash


if __name__ == "__main__":
    print()
    print("Generating new admin credentials...")
    print()
    
    creds = generate_credentials()
    print_setup_instructions(creds)
    
    # Also create a .env.example file
    with open(".env.example", "w") as f:
        f.write(f"""# Aegis One Environment Variables
# Copy this file to .env and fill in your values

# Admin Dashboard Password (required for /admin access)
ADMIN_PASSWORD={creds['password']}

# Database path (optional, defaults to reservations.sqlite)
# DB_PATH=reservations.sqlite
""")
    print("Created .env.example file")
    print()
