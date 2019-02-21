from django import forms

from .models import Filme

class Cadastro(forms.ModelForm):
    class Meta:
        model = Filme
        fields = ('Nome', 'Descricao', 'Url',)
