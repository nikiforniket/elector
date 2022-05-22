# -*- coding: utf-8 -*-

from django.contrib import admin
from voter.models import Voter


@admin.register(Voter)
class VoterAdmin(admin.ModelAdmin):

    list_display = ('id', 'first_name', 'last_name', 'age', 'gender', 'block', 'panchayat', 'created_by', 'created_at')
    list_filter = ('gender', 'block', 'panchayat')
    readonly_fields = ('created_at', 'updated_at', 'created_by')

    def save_model(self, request, obj, form, change):
        if not change:
            obj.created_by = request.user
        obj.save()
