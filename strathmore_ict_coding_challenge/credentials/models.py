from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings
from .utils.encryption import decrypt_key, encrypt_key, decrypt_key


class CustomUser(AbstractUser):
    encrypted_encryption_key = models.TextField(blank=True, null=True)
    is_admin = models.BooleanField(default=False)  # For role-based access

    def __str__(self):
        return self.username
    

class Credential(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    encrypted_content = models.TextField()

    def set_content(self, raw_content, password):
        # Decrypt user's encryption key using their password
        user_key = decrypt_key(self.owner.encrypted_encryption_key, password)
        encrypted = encrypt_key(raw_content.encode(), user_key.decode())
        self.encrypted_content = encrypted.decode()

    def get_content(self, password):
        user_key = decrypt_key(self.owner.encrypted_encryption_key, password)
        decrypted = decrypt_key(self.encrypted_content, user_key.decode())
        return decrypted.decode()

    def __str__(self):
        return f"{self.title} ({self.owner.username})"