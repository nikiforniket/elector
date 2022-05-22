# -*- coding: utf-8 -*-

from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth import get_user_model
from common.models import TimestampedModelMixin
from locations.models import (Panchayat,
                              Block)


class Voter(TimestampedModelMixin):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other')
    )
    OCCUPATION_TYPE = (
        ('P', 'Private'),
        ('G', 'Govt'),
        ('S', 'Self work'),
        ('U', 'Unemployed')
    )
    first_name = models.CharField(max_length=300)
    last_name = models.CharField(max_length=300)
    gender = models.CharField(choices=GENDER_CHOICES,
                              max_length=2)
    age = models.PositiveIntegerField(validators=[MaxValueValidator(130), MinValueValidator(15)])
    phone = models.CharField(max_length=10)
    email = models.EmailField(max_length=100,
                              null=True,
                              blank=True)
    occupation_type = models.CharField(choices=OCCUPATION_TYPE,
                                       max_length=3)
    block = models.ForeignKey(Block,
                              on_delete=models.SET_NULL,
                              null=True,
                              blank=True,
                              related_name='voters')
    panchayat = models.ForeignKey(Panchayat,
                                  on_delete=models.SET_NULL,
                                  null=True,
                                  blank=True,
                                  related_name='voters')
    created_by = models.ForeignKey(get_user_model(),
                                   on_delete=models.SET_NULL,
                                   null=True,
                                   blank=True,
                                   related_name='added_voters')
    updated_by = models.ForeignKey(get_user_model(),
                                   on_delete=models.SET_NULL,
                                   null=True,
                                   blank=True,
                                   related_name='updated_voters')


    def __str__(self):
        if self.block:
            return f"{self.name} | {self.age} | {self.gender} >>>> {self.block}"
        return f"{self.name} | {self.age} | {self.gender} >>>> {self.panchayat}"

    class Meta:
        verbose_name = "Voter"
        verbose_name_plural = "Voters"