"""module with views to be used in accounts app"""
from django.contrib.auth.views import LoginView, PasswordChangeView
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import SignUpForm

# pylint: disable=too-many-ancestors


class MyLoginView(LoginView):
    """view defined for logging in"""
    template_name = 'form.html'


class MyPasswordChangeView(PasswordChangeView):
    """view defined for changing password"""
    template_name = 'form.html'
    success_url = reverse_lazy('books')


class MySignUpView(CreateView):
    """view defined for signing up"""
    template_name = 'form.html'
    form_class = SignUpForm
    success_url = reverse_lazy('books')
