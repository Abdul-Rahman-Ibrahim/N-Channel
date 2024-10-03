from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = [
        'email',
        'username',
        'age',
        'is_staff'
    ]

    fieldsets = UserAdmin.fieldsets + (
        ('Position', {'fields': ('position',)}),
        ('Age', {'fields': ('age',)}),
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Email', {'fields': ('email',)}),
        ('Personal info', {'fields': ('first_name', 'last_name',)}),
        ('Position', {'fields': ('position',)}),
        ('Age', {'fields': ('age',)}),
    )

admin.site.register(CustomUser, CustomUserAdmin)
