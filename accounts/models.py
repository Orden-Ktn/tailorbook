from django.db import models
from django.db.models import F, Window
from django.db.models.functions import Rank
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth.models import AbstractUser
from django.conf import settings
import random


class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(unique=True)
    is_email_verified = models.BooleanField(default=False)
    verification_code = models.CharField(max_length=6, blank=True, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email
    
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