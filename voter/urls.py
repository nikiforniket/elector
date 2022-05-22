# -*- coding: utf-8 -*-

from django.urls import path
from voter.views import (AddVoterView,)

urlpatterns = [
    path('add-data/', AddVoterView.as_view(), name="add-data")
]