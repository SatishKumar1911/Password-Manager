from cryptography.fernet import Fernet

# Set a strong master password
master_password = "Satish@Kumar19".encode()

key = Fernet.generate_key()

with open("key.key", 'wb') as file:
    file.write(key)