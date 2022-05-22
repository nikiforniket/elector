# -*- coding: utf-8 -*-

from rest_framework.routers import DefaultRouter
from api import views

router = DefaultRouter()

router.register('c-data', views.AddVoterModelViewSet, basename='c-data')

urlpatterns = router.urls