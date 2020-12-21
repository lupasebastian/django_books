from django.contrib.auth.views import LoginView, PasswordChangeView
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView


class MyLoginView(LoginView):
    template_name = 'form.html'


class MyPasswordChangeView(PasswordChangeView):
    template_name = 'form.html'
    success_url = reverse_lazy('books')


class MySignUpView(CreateView):
    pass