# -*- coding: utf-8 -*-

import uuid
import re

from django.utils.translation import gettext_lazy as _
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import (AbstractUser,
                                        Permission,
                                        PermissionsMixin)
from django.core import validators
from userauth.managers import (ElectorUserManager,
                               ElectorDynamicUserManager)


class ElectoralUser(AbstractUser,
                    PermissionsMixin):
    """
    User model for electoral application
    Required Fields :: (email, full_name)
    """
    ROLES = (
        ('AD', 'Admin'),
        ('WK', 'Worker'),
        ('MN', 'Manager'),
        ('ST', 'Support'),
        ('IN', 'Internal')
    )
    uuid = models.UUIDField(default=uuid.uuid4,
                            editable=False)
    username = models.CharField(_("user name"),
                                max_length=32,
                                unique=True,
                                null=True,
                                blank=True,
                                help_text='Required. 30 characters or fewer. Letters, numbers and /./-/_characters',
                                validators=[validators.RegexValidator(re.compile(r"^[\w.-]+$"),
                                                                      "Enter a valid username.",
                                                                      "invalid")])
    email = models.EmailField(_("email"),
                              max_length=255,
                              null=False,
                              blank=False,
                              unique=True)
    role = models.CharField(max_length=10,
                            choices=ROLES,
                            default='IN')
    full_name = models.CharField(_("full name"),
                                 max_length=256,
                                 blank=False)
    is_superuser = models.BooleanField(default=False,
                                       verbose_name='superuser status',
                                       help_text="Designates whether the user can have access" 
                                                 "to all permissions on every model."
                                       )
    is_active = models.BooleanField(_('active status'),
                                    default=True,
                                    help_text="Designates whether this user should be treated as active." 
                                              "Unselect this instead of deleting accounts.")
    is_staff = models.BooleanField(_('staff status'),
                                   default=False,
                                   help_text="Designates whether the user can log into this admin site.")
    full_name = models.CharField(_("full name"),
                                 max_length=256,
                                 blank=True)
    bio = models.TextField(_("biography"),
                           null=False,
                           blank=True,
                           default="")
    photo = models.ImageField(upload_to='profile-pictures',
                              blank=True,
                              null=True)
    date_joined = models.DateTimeField(verbose_name='date joined',
                                       default=timezone.now)
    added_by = models.ForeignKey('ElectoralUser',
                                 related_name='added_by_elector_users',
                                 on_delete=models.SET_NULL,
                                 null=True,
                                 blank=True)

    objects = ElectorUserManager()

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['full_name']

    class Meta:
        verbose_name = 'Electoral User'
        verbose_name_plural = 'Electoral Users'
        ordering = ['full_name', '-date_joined']


class AdminUser(ElectoralUser):
    objects = ElectorDynamicUserManager('AD')

    class Meta:
        proxy = True
        verbose_name = "Admin User"
        verbose_name_plural = "Admin Users"


class ManagerUser(ElectoralUser):
    objects = ElectorDynamicUserManager('MN')

    class Meta:
        proxy = True
        verbose_name = "Manager User"
        verbose_name_plural = "Manager Users"


class WorkerUser(ElectoralUser):
    objects = ElectorDynamicUserManager('WK')

    class Meta:
        proxy = True
        verbose_name = "Worker User"
        verbose_name_plural = "Worker Users"