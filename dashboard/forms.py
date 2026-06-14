from django import forms
from .models import *
from django.contrib.auth.forms import *


class DepenseForm(forms.ModelForm):
    class Meta:
        model = Depense
        fields = ['motif', 'montant']
        widgets = {
            'motif': forms.Textarea(attrs={
                'class': 'form-input',
                'rows': 3,
                'style': 'resize: vertical; min-height: 80px;',
            }),
            'montant': forms.TextInput(attrs={'class': 'form-input'}),
        }

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None) 
        super().__init__(*args, **kwargs)

    def clean_motif(self):
        nom = (self.cleaned_data.get("motif") or "").strip()
        
        qs = Depense.objects.all()
        if self.user:
            qs = qs.filter(atelier=self.user)

        # 🔹 Exclure l'objet en cours si on est en modification
        if self.instance.pk:
            qs = qs.exclude(pk=self.instance.pk)

        return nom

