from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import CustomUser
from .utils.encryption import generate_user_key, encrypt_key

@receiver(post_save, sender=CustomUser)
def create_encryption_key(sender, instance, created, **kwargs):
    if created and not instance.encrypted_encryption_key:
        # Use the user's password to encrypt their key
        raw_key = generate_user_key()
        encrypted = encrypt_key(raw_key, instance.password)
        instance.encrypted_encryption_key = encrypted
        instance.save()