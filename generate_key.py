import base64
import os
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

# Set a strong master password
master_password = b"Satish@Kumar19"

# Generate a random salt
salt = os.urandom(16)

# Use PBKDF2HMAC to derive a key from the master password
kdf = PBKDF2HMAC(
    algorithm=hashes.SHA256(),
    length=32,
    salt=salt,
    iterations=100000,  # Increase iterations for better security
)
key = base64.urlsafe_b64encode(kdf.derive(master_password))


with open("key.key", 'wb') as file:
    file.write(key)