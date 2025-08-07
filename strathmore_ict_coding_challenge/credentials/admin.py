from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from .models import Credential


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['username', 'email', 'is_admin', 'is_active']
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('encrypted_encryption_key', 'is_admin')}),
    )

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Credential)
