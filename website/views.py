# -*- coding: utf-8 -*-

from django.shortcuts import (render,
                              redirect)
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin


class HomePage(LoginRequiredMixin, View):

    template_name = 'website/home.html'

    def get(self, request, *args, **kwargs):
        return render(request,
                      self.template_name,
                      status=200)