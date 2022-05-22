# -*- coding: utf-8 -*-

from rest_framework import serializers
from voter.models import Voter
from locations.models import (Panchayat,
                              Block)


class AddUpdateVoterSerializer(serializers.ModelSerializer):

    class Meta:
        model = Voter
        fields = ('id', 'first_name', 'last_name', 'gender', 'occupation_type',
                  'age', 'phone', 'email', 'block', 'panchayat', 'created_by', 'updated_by')


class PanchayatSelect2Serializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()

    def get_name(self, instance):
        return str(instance)

    class Meta:
        model = Panchayat
        fields = ('id', 'name')


class BlockSelect2Serializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()

    def get_name(self, instance):
        return str(instance)

    class Meta:
        model = Block
        fields = ('id', 'name')