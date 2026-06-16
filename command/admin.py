from django.contrib import admin
from .models import Commande

@admin.register(Commande)
class CommandeAdmin(admin.ModelAdmin):
    list_display = ('id', 'client', 'atelier', 'montant', 'avance', 'depense', 'get_revenu', 'get_reste', 'statut', 'date_livraison', 'date_commande')
    list_filter = ('statut', 'atelier')
    search_fields = ('client__nom_prenom',)
    ordering = ('-date_commande',)

    @admin.display(description='Revenu')
    def get_revenu(self, obj):
        return obj.revenu()

    @admin.display(description='Reste à payer')
    def get_reste(self, obj):
        return obj.reste_a_payer()