from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm

class usuario_form (UserCreationForm):
    Sexo = (
        ('Hombre', 'Hombre'),
        ('Mujer', 'Mujer'),
    )
    nombre =forms.CharField(max_length=24)
    apellidos =forms.CharField(max_length=24)
    edad =forms.FloatField()
    sexo = forms.ChoiceField(choices = Sexo)
    email = forms.CharField(max_length = 50)

    
    

    