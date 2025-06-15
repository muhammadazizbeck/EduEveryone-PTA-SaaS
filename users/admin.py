# admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import CustomUser

@admin.register(CustomUser)
class UserAdmin(BaseUserAdmin):
    list_display = ("email", "full_name", "user_type", "disability_type", "is_staff")
    list_filter  = ("user_type", "disability_type", "is_staff", "is_active")
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        ("Personal info", {"fields": ("full_name", "user_type", "disability_type")}),
        ("Permissions", {"fields": ("is_active", "is_staff", "is_superuser", "groups", "user_permissions")}),
        ("Important dates", {"fields": ("last_login",)}),
    )
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("email", "full_name", "password1", "password2", "user_type", "disability_type", "is_active", "is_staff"),
        }),
    )
    search_fields = ("email", "full_name")
    ordering = ("email",)

