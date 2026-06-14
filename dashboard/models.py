from django.db import models
from django.contrib.auth.models import User
from django.conf import settings



class Depense(models.Model):
    atelier = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="depenses"
    )
    motif = models.CharField(max_length=255)
    montant = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.motif} - {self.montant}"

    class Meta:
        ordering = ['-id']