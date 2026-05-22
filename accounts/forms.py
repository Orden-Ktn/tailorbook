from django import forms
from .models import CustomUser, Profile
from django.contrib.auth.forms import *

class CustomUserCreationForm(forms.ModelForm):
    password = forms.CharField(
        label="Mot de passe",
        widget=forms.PasswordInput(),
        help_text="Votre mot de passe doit contenir au moins 8 caractères."
    )

    class Meta:
        model = CustomUser
        fields = ['email']  # uniquement email + mot de passe

    def clean_email(self):
        email = self.cleaned_data.get("email").lower()
        if CustomUser.objects.filter(email=email).exists():
            raise forms.ValidationError("Cet email est déjà utilisé.")
        return email

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user

class VerificationCodeForm(forms.Form):
    code = forms.CharField(max_length=6, label="Code de vérification")


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['nom_atelier', 'contact', 'adresse']


class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
