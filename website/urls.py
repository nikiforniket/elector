# -*- coding: utf-8 -*-

from django.urls import path
from website.views import (HomePage,)

urlpatterns = [
    path('', HomePage.as_view(), name="home")
]