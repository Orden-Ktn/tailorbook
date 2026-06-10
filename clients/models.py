from django.conf import settings
from django.db import models
from django.contrib.auth.models import User


class Client(models.Model):
    SEXE_CHOICES = (
        ('M', 'Masculin'),
        ('F', 'Féminin'),
    )

    atelier = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="clients"
    )
    nom_prenom = models.CharField(max_length=100)
    sexe = models.CharField(max_length=1, choices=SEXE_CHOICES)
    telephone = models.CharField(max_length=20)
    adresse = models.TextField(blank=True)
    date_creation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nom_prenom



class MesureHomme(models.Model):
    client = models.OneToOneField(Client, on_delete=models.CASCADE)

    epaule_dos = models.FloatField(blank=True, null=True)
    tour_poitrine = models.FloatField(blank=True, null=True)
    tour_manche = models.FloatField(blank=True, null=True)
    longueur_manche = models.FloatField(blank=True, null=True)
    longueur_bohumba = models.FloatField(blank=True, null=True)
    tour_cou = models.FloatField(blank=True, null=True)
    longueur_chemise = models.FloatField(blank=True, null=True)
    ceinture = models.FloatField(blank=True, null=True)
    tour_hanche = models.FloatField(blank=True, null=True)
    longueur_pantalon = models.FloatField(blank=True, null=True)
    longueur_genou = models.FloatField(blank=True, null=True)
    tour_genou = models.FloatField(blank=True, null=True)
    tour_bas = models.FloatField(blank=True, null=True)
    tour_cuisse = models.FloatField(blank=True, null=True)
    longueur_culotte = models.FloatField(blank=True, null=True)
    longueur_gilet = models.FloatField(blank=True, null=True)
    longueur_veste = models.FloatField(blank=True, null=True)

    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Mesure Homme - {self.client.nom}"


class MesureFemme(models.Model):
    client = models.OneToOneField(Client, on_delete=models.CASCADE)

    epaule_dos = models.FloatField(blank=True, null=True)
    tour_poitrine = models.FloatField(blank=True, null=True)
    longueur_manche = models.FloatField(blank=True, null=True)
    tour_manche = models.FloatField(blank=True, null=True)
    carrure_devant = models.FloatField(blank=True, null=True)
    carrure_dos = models.FloatField(blank=True, null=True)
    longueur_sein = models.FloatField(blank=True, null=True)
    longueur_corsage = models.FloatField(blank=True, null=True)
    tour_taille = models.FloatField(blank=True, null=True)
    ceinture = models.FloatField(blank=True, null=True)
    tour_hanche = models.FloatField(blank=True, null=True)
    longueur_clotop = models.FloatField(blank=True, null=True)
    longueur_robe = models.FloatField(blank=True, null=True)
    longueur_jupe = models.FloatField(blank=True, null=True)
    longueur_chambrage_dos = models.FloatField(blank=True, null=True)
    longueur_bohumba = models.FloatField(blank=True, null=True)
    ecart_seins = models.FloatField(blank=True, null=True)

    longueur_pantalon = models.FloatField(blank=True, null=True)
    longueur_genou = models.FloatField(blank=True, null=True)
    longueur_taille_devant = models.FloatField(blank=True, null=True)
    longueur_taille_dos = models.FloatField(blank=True, null=True)
    tour_bas = models.FloatField(blank=True, null=True)
    tour_encolure = models.FloatField(blank=True, null=True)

    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Mesure Femme - {self.client.nom}"
