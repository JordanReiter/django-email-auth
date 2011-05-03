from django import forms
from django.contrib.auth.forms import AuthenticationForm as AuthAuthenticationForm
from django.contrib.auth.models import User 

class AuthenticationForm(AuthAuthenticationForm):
    username = forms.EmailField(max_length=75)