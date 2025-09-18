from django import forms

from . import models
from .models import ContactModel
from django.contrib.auth.forms import AuthenticationForm


class ContactForm(forms.ModelForm):
    class Meta:
        model = models.ContactModel
        fields = "__all__"


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Username'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Password'
    }))
