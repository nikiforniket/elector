# -*- coding: utf-8 -*-

from django.contrib import admin
from locations.models import (State, District,
                              Constituency, Block,
                              Panchayat)

@admin.register(State)
class StateAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_at', 'updated_at')
    readonly_fields = ('created_at', 'updated_at')


@admin.register(District)
class DistrictAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'state', 'created_at', 'updated_at')
    list_filter = ('state',)
    readonly_fields = ('created_at', 'updated_at')


@admin.register(Constituency)
class ConstituencyAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'district', 'created_at', 'updated_at')
    list_filter = ('district',)
    readonly_fields = ('created_at', 'updated_at')


@admin.register(Block)
class BlockAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'district', 'constituency')
    list_filter = ('district', 'constituency')
    readonly_fields = ('created_at', 'updated_at')


@admin.register(Panchayat)
class PanchayatAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'block')
    list_filter = ('block',)
    readonly_fields = ('created_at', 'updated_at')