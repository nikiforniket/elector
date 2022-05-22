# -*- coding: utf-8 -*-

from django.contrib.auth.models import BaseUserManager
from django.db.models import Manager


class ElectorUserManager(BaseUserManager):
    """ User manager for users of elector application """

    def create_user(self, email, full_name, password):
        if not email:
            raise ValidationError('Email is required.')
        if not full_name:
            raise ValidationError('Full name is required')
        if not password:
            raise ValidationError('Password is required.')
        user = self.model(email=self.normalize_email(email), full_name=full_name)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, full_name, password):
        if not email:
            raise ValidationError('Email is required.')
        if not full_name:
            raise ValidationError('Full name is required')
        if not password:
            raise ValidationError('Password is required.')
        user = self.model(email=self.normalize_email(email), full_name=full_name)
        user.is_superuser = True
        user.is_staff = True
        user.set_password(password)
        user.save(using=self._db)
        return user


class ElectorDynamicUserManager(Manager):
    """ Dynamic User Manager to handle multiple roles """

    def __init__(self, user_type):
        super(ElectorDynamicUserManager, self).__init__()
        self.user_type = user_type

    def get_queryset(self):
        return super(ElectorDynamicUserManager, self).get_queryset().filter(role=self.user_type)

    def create(self, *args, **kwargs):
        kwargs['role'] = self.user_type
        return super(ElectorDynamicUserManager, self).create(*args, **kwargs)
