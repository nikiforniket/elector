# -*- coding: utf-8 -*-

from django.db import models
from common.models import TimestampedModelMixin


class State(TimestampedModelMixin):
    """ State Model """
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "State"
        verbose_name_plural = "States"
        ordering = ['name']


class District(TimestampedModelMixin):
    """ Distict Model to be mapped under State """
    name = models.CharField(max_length=200)
    state = models.ForeignKey(State, on_delete=models.CASCADE, related_name='districts')

    def __str__(self):
        return f"{self.state} >> {self.name} District"

    class Meta:
        verbose_name = "District"
        verbose_name_plural = "Districts"
        ordering = ['name', 'state__name']


class Constituency(TimestampedModelMixin):
    """Constiuencies mapped under districts"""
    name = models.CharField(max_length=200)
    district = models.ForeignKey(District, on_delete=models.CASCADE, related_name='constituencies')

    def __str__(self):
        return f"{self.district} >> {self.name} Constituency"

    class Meta:
        verbose_name = "Constituency"
        verbose_name_plural = "Constituencies"
        ordering = ['name', 'district__name']


class Block(TimestampedModelMixin):
    """Blocks mapped under a district or constituency"""
    name = models.CharField(max_length=200)
    district = models.ForeignKey(District,
                                 on_delete=models.CASCADE,
                                 related_name='blocks')
    constituency = models.ForeignKey(Constituency,
                                     on_delete=models.SET_NULL,
                                     related_name='blocks',
                                     null=True,
                                     blank=True)

    def __str__(self):
        return f"{self.district} >> {self.name} Block"

    class Meta:
        verbose_name = "Block"
        verbose_name_plural = "Blocks"
        ordering = ['name', 'district__name']


class Panchayat(TimestampedModelMixin):
    """ Panchayat mapped under a block """
    name = models.CharField(max_length=200)
    block = models.ForeignKey(Block, on_delete=models.SET_NULL,
                              related_name='panchayats',
                              null=True,
                              blank=True)
    constituency = models.ForeignKey(Constituency,
                                     on_delete=models.CASCADE,
                                     related_name='panchayats')

    def __str__(self):
        return f"{self.block} >> {self.name} Panchayat"

    class Meta:
        verbose_name = "Panchayat"
        verbose_name_plural = "Panchayats"
        ordering = ['name', 'block__name', 'constituency__name']