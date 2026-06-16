from django.db import models
from clients.models import Client
from django.conf import settings


class Commande(models.Model):
    STATUT_CHOICES = (
        ('recue', 'Reçue'),
        ('achevee', 'Achevée'),
        ('livree', 'Livrée'),
    )

    atelier = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="commandes"
    )
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name="commandes")
    statut = models.CharField(max_length=20, choices=STATUT_CHOICES, default='debuter')
    montant = models.DecimalField(max_digits=10, decimal_places=2)
    depense = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    avance = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    date_commande = models.DateTimeField(auto_now_add=True)
    date_livraison = models.DateField()

    def reste_a_payer(self):
        return self.montant - self.avance
    
    def revenu(self):
        return self.montant - self.depense

    def __str__(self):
        return f"Commande #{self.id} - {self.client}"
