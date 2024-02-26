# Run this file manually once before running the password_manage.py

from cryptography.fernet import Fernet

key = Fernet.generate_key()

with open("key.key", 'wb') as file:
    file.write(key)
