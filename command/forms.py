from django import forms
from .models import *
from django.contrib.auth.forms import *


class CommandeForm(forms.ModelForm):
    class Meta:
        model = Commande
        fields = ['client', 'montant', 'avance', 'date_livraison']
        widgets = {
            'client': forms.Select(attrs={'class': 'form-select'}),
            'montant': forms.NumberInput(attrs={'class': 'form-input'}),
            'avance': forms.NumberInput(attrs={'class': 'form-input'}),
            'date_livraison': forms.DateInput(attrs={
                'class': 'form-input',
                'type': 'date'
            }),
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)

        if user:
            self.fields['client'].queryset = Client.objects.filter(atelier=user)
