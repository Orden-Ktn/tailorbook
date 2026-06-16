from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from accounts.models import ModeleAtelier, Profile
from clients.models import Client
from command.models import Commande
from .models import *
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q
from django.contrib.auth import logout
from django.db.models import Sum, F, ExpressionWrapper, DecimalField
from django.contrib.auth.models import User
from .models import *
from .forms import *
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import DepenseForm




@login_required 
def dashboard(request):
    user = request.user

    total_client = Client.objects.filter(atelier=user).count()
    total_client_h = Client.objects.filter(sexe='M', atelier=user).count()
    total_client_f = Client.objects.filter(sexe='F', atelier=user).count()
    total_commande_recue = Commande.objects.filter(client__atelier=user).count()
    total_commande_livree = Commande.objects.filter(statut='livree', client__atelier=user).count()
    # Total des revenus : sommes des avances des commandes achevées
    total_recette = Commande.objects.filter(client__atelier=user).aggregate(
        total=Sum('avance')
    )['total'] or 0

    # Total restant à payer : somme de (montant - avance) des commandes achevées
    total_reste = Commande.objects.filter(statut='livree').aggregate(
        total=Sum(ExpressionWrapper(F('montant') - F('avance'), output_field=DecimalField()))
    )['total'] or 0

    total_depenses = Commande.objects.filter(atelier=user).aggregate(
        total=Sum('depense')
    )['total'] or 0

    revenu = total_recette - total_depenses

    context = {
        'total_client': total_client,
        'total_client_h': total_client_h,
        'total_client_f': total_client_f,
        'total_commande_recue': total_commande_recue,
        'total_commande_livree': total_commande_livree,
        'total_recette': total_recette,
        'total_reste': total_reste,
        'total_depenses': total_depenses,
        'revenu': revenu,
    }

    return render(request, 'dashboard.html', context)


def deconnexion(request):
    logout(request)
    return redirect('login')



@login_required
def mes_modeles(request):
    modeles = ModeleAtelier.objects.filter(tailleur=request.user)
    nb_modeles = modeles.count()
    peut_ajouter = nb_modeles < 5

    if request.method == 'POST':
        if not peut_ajouter:
            messages.error(request, "Vous avez atteint la limite de 5 modèles.")
            return redirect('modeles')
        
        image = request.FILES.get('image')
        description = request.POST.get('description', '')

        if not image:
            messages.error(request, "Veuillez sélectionner une image.")
            return redirect('modeles')

        # Vérifier les types de fichiers autorisés
        allowed_types = ['image/jpeg', 'image/png', 'image/webp']
        if image.content_type not in allowed_types:
            messages.error(request, "Format non supporté. Utilisez JPG, PNG ou WEBP.")
            return redirect('modeles')

        ModeleAtelier.objects.create(
            tailleur=request.user,
            image=image,
            description=description
        )
        messages.success(request, "Modèle ajouté avec succès !")
        return redirect('modeles')

    return render(request, 'modeles.html', {
        'modeles': modeles,
        'nb_modeles': nb_modeles,
        'peut_ajouter': peut_ajouter,
        'max_modeles': 5,
    })


@login_required
def supprimer_modele(request, modele_id):
    modele = get_object_or_404(ModeleAtelier, id=modele_id, tailleur=request.user)
    if request.method == 'POST':
        modele.image.delete(save=False)
        modele.delete()
        messages.success(request, "Modèle supprimé.")
    return redirect('modeles')



@login_required
def depenses(request):
    form = DepenseForm(user=request.user)

    if request.method == 'POST':
        depense_id = request.POST.get('depense_id')

        if depense_id:  # Modification
            depense = get_object_or_404(Depense, pk=depense_id, atelier=request.user)
            form = DepenseForm(request.POST, instance=depense, user=request.user)
        else:  # Ajout
            form = DepenseForm(request.POST, user=request.user)

        if form.is_valid():
            depense = form.save(commit=False)
            depense.atelier = request.user
            depense.save()
            return redirect('depenses')
        # Si invalide, le form avec erreurs sera affiché

    qs = Depense.objects.filter(atelier=request.user).order_by('-id')
    paginator = Paginator(qs, 10)
    page = request.GET.get('page')

    try:
        depense_page = paginator.page(page)
    except PageNotAnInteger:
        depense_page = paginator.page(1)
    except EmptyPage:
        depense_page = paginator.page(paginator.num_pages)

    return render(request, 'depenses.html', {
        'form': form,
        'depense': depense_page,
    })



@login_required
def modifier_depense(request, pk):
    depense = get_object_or_404(Depense, pk=pk, atelier=request.user)
    if request.method == 'POST':
        form = DepenseForm(request.POST, instance=depense, user=request.user)
        if form.is_valid():
            form.save()
    return redirect('depenses')


@login_required
def supprimer_depense(request, pk):
    depense = get_object_or_404(Depense, pk=pk, atelier=request.user)
    depense.delete()
    return redirect('depenses')


