# -*- coding: utf-8 -*-

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from userauth.models import ElectoralUser
from userauth.forms import (ElectoralUserChangeForm,
                            ElectoralUserCreationForm)


@admin.register(ElectoralUser)
class ElectoralUserAdmin(UserAdmin):
    form = ElectoralUserChangeForm
    add_form = ElectoralUserCreationForm

    fieldsets = (
        (
            "User", {
                "fields": ('uuid', 'email', 'username', 'password')
            }
        ),
        (
            "Role", {
                "fields": ('role',)
            }
        ),
        (
            "Other Information", {
                "fields": ('full_name', 'bio', 'photo', 'date_joined')
            }
        )
    )

    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ('email', 'full_name', 'username',
                       "password", "confirm_password"),
        }),
    )
    list_display = ('uuid', 'email', 'username', 'role', 'is_active', 'is_staff', 'is_superuser', 'last_login', 'date_joined')
    list_filter = ('role', 'is_active', 'is_superuser', 'is_staff')
    search_fields = ('email',)