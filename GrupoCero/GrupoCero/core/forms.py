from dataclasses import fields
from pyexpat import model
from django import forms
from .models import Contacto,Arte
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .validators import ValidationError
from django.forms import ValidationError


class ContactoForm(forms.ModelForm):
    class Meta:
        model = Contacto
        fields = '__all__'


class ArteForm(forms.ModelForm):
    nombre = forms.CharField(min_length=3,max_length=20)
    precio = forms.IntegerField(min_value=1)
    class Meta:
        model = Arte
        fields= '__all__'

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username","first_name","last_name","email","password1","password2"]