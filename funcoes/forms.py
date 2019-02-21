from django import forms

from .models import Filme

class Cadastro(forms.ModelForm):
    nome = forms.CharField(required = False)
