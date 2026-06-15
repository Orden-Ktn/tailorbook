from django import forms
from .models import CustomUser, Profile
from django.contrib.auth.forms import *

class CustomUserCreationForm(forms.ModelForm):
    password = forms.CharField(
        label="Mot de passe",
        widget=forms.PasswordInput(),
        help_text="Votre mot de passe doit contenir au moins 8 caractères."
    )
    username = forms.CharField(
        label="Nom d'utilisateur",
        help_text="Le nom d'utilisateur doit être unique.",
        widget=forms.TextInput(attrs={'placeholder': "Entrez votre nom d'utilisateur. Ex: 'toto123'"})
    )

    class Meta:
        model = CustomUser
        fields = ['username']

    def clean_username(self):
        username = self.cleaned_data.get("username")
        if CustomUser.objects.filter(username=username).exists():
            raise forms.ValidationError("Ce nom d'utilisateur est déjà utilisé.")
        return username

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user


class LoginForm(forms.Form):
    username = forms.CharField(label="Nom d'utilisateur")
    password = forms.CharField(widget=forms.PasswordInput)


class ProfileForm(forms.ModelForm):
    contact = forms.CharField(
        label="Contact",
        help_text="Le contact doit être votre numéro WhatsApp de préférence.",
        widget=forms.TextInput(attrs={'placeholder': "Ex: 0144332211"})
    )
    
    class Meta:
        model = Profile
        fields = ['nom_atelier', 'contact', 'adresse']

    def clean_contact(self):
        contact = self.cleaned_data.get('contact', '')
        # Retire espaces, tirets, parenthèses
        contact = contact.strip().replace(' ', '').replace('-', '').replace('(', '').replace(')', '')
        
        # Cas 1 : déjà au format international complet +2290XXXXXXXX (13 chiffres avec 01)
        if contact.startswith('+2290'):
            return contact  # ✅ +2290162992332
        
        # Cas 2 : +229 sans le 0 → +22962992332 (ancien format)
        if contact.startswith('+229'):
            numero = contact[4:]  # extrait les chiffres après +229
            if len(numero) == 8:  # ancien format 8 chiffres → ajoute 01
                return '+2290' + '1' + numero  # ⚠️ à adapter selon votre logique
            return contact  # laisse tel quel sinon
        
        # Cas 3 : commence par 229 sans le +
        if contact.startswith('229'):
            return '+' + contact
        
        # Cas 4 : commence par 0 → 0162992332
        if contact.startswith('0'):
            return '+229' + contact  # garde le 0 → +2290162992332
        
        # Cas 5 : numéro court sans rien → 62992332 (8 chiffres, ancien format)
        if len(contact) == 8:
            return '+229' + contact  # → +22962992332
        
        # Cas 6 : 10 chiffres avec 01 mais sans indicatif → 0162992332
        if len(contact) == 10:
            return '+229' + contact  # → +2290162992332

        return contact