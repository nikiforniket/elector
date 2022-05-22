# -*- coding: utf-8 -*-

from django.shortcuts import (render,
                              redirect)
from django.views import View
from django.contrib.auth import (authenticate,
                                 login,
                                 logout)
from userauth.models import ElectoralUser


class LoginView(View):

    template_name = 'auth/login.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        email, password = request.POST.get('email'), request.POST.get('password')
        try:
            ElectoralUser.objects.get(email=email)
            user = authenticate(request,
                                email=email,
                                password=password)
            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                return render(request,
                              self.template_name,
                              context={
                                    'password_error': 'Password entered is wrong.',
                                    'email': email
                              }, status=400)
        except ElectoralUser.DoesNotExist:
            return render(request,
                          self.template_name,
                          context={
                              'email_error': 'Email does not exist on our system.'
                          }, status=400)


class LogOutView(View):

    def get(self, request):
        logout(request)
        return redirect('userauth:login')