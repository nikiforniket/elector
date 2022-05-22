# -*- coding: utf-8 -*-
from rest_framework import (mixins,
                            viewsets,
                            status)
from rest_framework.views import (APIView,)
from rest_framework.permissions import (IsAuthenticated,
                                        AllowAny)

from voter.models import Voter
from api.serializers import (AddUpdateVoterSerializer,
                             PanchayatSelect2Serializer,
                             BlockSelect2Serializer)


class AddVoterModelViewSet(viewsets.GenericViewSet,
                           mixins.CreateModelMixin):
    serializer_class = AddUpdateVoterSerializer
    permission_classes = [IsAuthenticated,]

    def get_queryset(self):
        return Voter.objects.all()


class PanchayatSelect2ViewSet(viewsets.GenericViewSet,
                              mixins.ListModelMixin):
    serializer_class = PanchayatSelect2Serializer
    permission_classes = [IsAuthenticated,]

    def list(self, request, *args, **kwargs):
        search = self.request.query_params.get('search')

