"""module for dispatching urls"""
from django.contrib.auth.views import LogoutView
from django.urls import path

from .views import MyLoginView, MyPasswordChangeView, MySignUpView

urlpatterns = [
    path('login/', MyLoginView.as_view(), name='login'),
    path('password-change/', MyPasswordChangeView.as_view(), name='password-change'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('sign-up/', MySignUpView.as_view(), name='sign-up'),
]
