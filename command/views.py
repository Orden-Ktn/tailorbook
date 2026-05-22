from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *
from django.contrib import messages
from django.db.models import Sum, F, ExpressionWrapper, DecimalField
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

@login_required
def commande(request):
    user = request.user
    
    form = CommandeForm(request.POST or None, user=user)

    # ✅ Commandes de l'utilisateur connecté
    commande_qs = Commande.objects.filter(client__atelier=user)

    # ✅ Clients de l'utilisateur connecté
    client = Client.objects.filter(atelier=user)

    # Pagination
    paginator = Paginator(commande_qs, 10)
    page = request.GET.get('page')
    
    try:
        commandes = paginator.page(page)
    except PageNotAnInteger:
        commandes = paginator.page(1)
    except EmptyPage:
        commandes = paginator.page(paginator.num_pages)

    return render(request, 'commande.html', {
        "form": form,
        'commande': commandes,
        'client': client,
    })


@login_required
def ajouter_commande(request):
    if request.method == "POST":
        command_id = request.POST.get("command_id")

        # 🔹 MODIFICATION
        if command_id:
            commande = get_object_or_404(Commande, id=command_id)
            form = CommandeForm(request.POST, instance=commande, user=request.user)

            if form.is_valid():
                form.save()
                messages.success(request, "Commande modifiée avec succès !")
                return redirect("commande")
            else:
                print(form.errors)

        # 🔹 AJOUT
        else:
            form = CommandeForm(request.POST, user=request.user)

            if form.is_valid():
                commande = form.save(commit=False)
                commande.statut = 'recue'
                commande.save()
                messages.success(request, "Commande enregistrée avec succès !")
                return redirect("commande")
            else:
                print(form.errors)

    else:
        form = CommandeForm(user=request.user)

    return render(request, "commande.html", {"form": form})


@login_required
def supprimer_commande(request, commande_id):
    commande = get_object_or_404(Commande, id=commande_id)
    commande.delete()
    messages.success(request, "Commande supprimée avec succès.")
    return redirect('commande')



@login_required
def terminer_commande(request, commande_id):
    commande = get_object_or_404(Commande, id=commande_id)
    
    # Mettre à jour le statut
    commande.statut = 'livree'
    commande.avance = commande.montant
    commande.save()

    messages.success(request, f"La commande de {commande.client.nom_prenom} est maintenant livrée.")
    return redirect('commande')


