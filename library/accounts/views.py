from django.contrib.auth.views import LoginView, PasswordChangeView
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import SignUpForm


class MyLoginView(LoginView):
    template_name = 'form.html'


class MyPasswordChangeView(PasswordChangeView):
    template_name = 'form.html'
    success_url = reverse_lazy('books')


class MySignUpView(CreateView):
    template_name = 'form.html'
    form_class = SignUpForm
    success_url = reverse_lazy('books')
