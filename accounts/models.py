from django.db import models
from django.db.models import F, Window
from django.db.models.functions import Rank
from django.contrib.auth.hashers import make_password, check_password
from django.conf import settings
import random
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.core.exceptions import ValidationError

class CustomUserManager(BaseUserManager):
    def create_user(self, username, password=None, **extra_fields):
        if not username:
            raise ValueError("Le nom d'utilisateur est obligatoire")
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(username, password, **extra_fields)


class CustomUser(AbstractUser):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(blank=True, null=True)
    is_email_verified = models.BooleanField(default=False)
    verification_code = models.CharField(max_length=6, blank=True, null=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.username

    def generate_verification_code(self):
        code = str(random.randint(100000, 999999))
        self.verification_code = code
        self.save()
        return code


class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    nom_atelier = models.CharField(max_length=150)
    contact = models.CharField(max_length=20)
    adresse = models.CharField(max_length=100)

    def __str__(self):
        return self.nom_atelier
    
    @property
    def whatsapp_url(self):
        # Retire le + pour l'URL wa.me
        number = self.contact.replace('+', '').replace(' ', '')
        return f"https://wa.me/{number}"


class ModeleAtelier(models.Model):
    tailleur = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='modeles')
    image = models.ImageField(upload_to='')
    description = models.CharField(max_length=200, blank=True)
    date_ajout = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Modèle d'atelier"
        verbose_name_plural = "Modèles d'atelier"
        ordering = ['-date_ajout']

    def __str__(self):
        return f"Modèle de {self.tailleur.get_full_name() or self.tailleur.username}"

    def clean(self):
        if self.tailleur and ModeleAtelier.objects.filter(tailleur=self.tailleur).exclude(pk=self.pk).count() >= 5:
            raise ValidationError("Un atelier ne peut pas avoir plus de 5 modèles.")