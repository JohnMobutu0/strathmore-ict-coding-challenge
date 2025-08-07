from cryptography.fernet import Fernet
import base64
import hashlib

def generate_user_key():
    return Fernet.generate_key()

def derive_key_from_password(password):
    # Derive a key from the user's password using SHA256
    return base64.urlsafe_b64encode(hashlib.sha256(password.encode()).digest())

def encrypt_key(user_key, password):
    derived_key = derive_key_from_password(password)
    f = Fernet(derived_key)
    return f.encrypt(user_key).decode()

def decrypt_key(encrypted_key, password):
    derived_key = derive_key_from_password(password)
    f = Fernet(derived_key)
    return f.decrypt(encrypted_key.encode())