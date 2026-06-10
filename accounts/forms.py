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

