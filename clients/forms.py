from django import forms
from .models import *
from django.contrib.auth.forms import *


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['nom_prenom', 'telephone', 'adresse', 'sexe']
        widgets = {
            'nom_prenom': forms.TextInput(attrs={'class': 'form-input'}),
            'telephone': forms.TextInput(attrs={'class': 'form-input'}),
            'adresse': forms.TextInput(attrs={'class': 'form-input'}),
            'sexe': forms.Select(attrs={'class': 'form-select'}),
        }

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)  # récupère l'utilisateur si passé
        super().__init__(*args, **kwargs)

    def clean_nom_prenom(self):
        nom = (self.cleaned_data.get("nom_prenom") or "").strip()
        
        qs = Client.objects.all()
        if self.user:
            qs = qs.filter(atelier=self.user)

        # 🔹 Exclure l'objet en cours si on est en modification
        if self.instance.pk:
            qs = qs.exclude(pk=self.instance.pk)

        if qs.filter(nom_prenom__iexact=nom).exists():
            raise forms.ValidationError("Un client avec ce nom existe déjà.")
        
        return nom



class MesureFemmeForm(forms.ModelForm):

    class Meta:
        model = MesureFemme
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)

        if user:
            self.fields['client'].queryset = Client.objects.filter(
                atelier=user,
                sexe='F'
            )

        for field in self.fields.values():
            field.widget.attrs.update({
                'class': 'form-input'
            })



class MesureHommeForm(forms.ModelForm):

    class Meta:
        model = MesureHomme
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)

        if user:
            self.fields['client'].queryset = Client.objects.filter(
                atelier=user,
                sexe='M'
            )

        for field in self.fields.values():
            field.widget.attrs.update({
                'class': 'form-input'
            })


