from django.shortcuts import render

from accounts.models import CustomUser, ModeleAtelier, Profile


def accueil(request):
    return render(request, 'accueil.html')


def galerie_tailleurs(request):
    tailleurs = CustomUser.objects.filter(modeles__isnull=False).distinct()
    
    ateliers = []
    for tailleur in tailleurs:
        modeles = ModeleAtelier.objects.filter(tailleur=tailleur)[:10]
        try:
            contact = tailleur.profile.contact
        except Profile.DoesNotExist:
            contact = None
        
        ateliers.append({
            'tailleur': tailleur,
            'modeles': modeles,
            'contact': contact,
            'profile': getattr(tailleur, 'profile', None),  
            'nom_atelier': getattr(getattr(tailleur, 'profil', None), 'nom_atelier', '') or tailleur.get_full_name() or tailleur.username,
        })
    
    return render(request, 'galerie.html', {'ateliers': ateliers})


