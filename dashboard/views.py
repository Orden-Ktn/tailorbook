from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from clients.models import Client
from command.models import Commande
from .models import *
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q
from django.contrib.auth import logout
from django.db.models import Sum, F, ExpressionWrapper, DecimalField


@login_required 
def dashboard(request):
    user = request.user

    total_client = Client.objects.filter(atelier=user).count()
    total_client_h = Client.objects.filter(sexe='M', atelier=user).count()
    total_client_f = Client.objects.filter(sexe='F', atelier=user).count()
    total_commande_recue = Commande.objects.filter(client__atelier=user).count()
    total_commande_livree = Commande.objects.filter(statut='livree', client__atelier=user).count()
    # Total des revenus : sommes des avances des commandes achevées
    total_revenus = Commande.objects.filter(client__atelier=user).aggregate(
        total=Sum('avance')
    )['total'] or 0

    # Total restant à payer : somme de (montant - avance) des commandes achevées
    total_reste = Commande.objects.filter(statut='livree').aggregate(
        total=Sum(ExpressionWrapper(F('montant') - F('avance'), output_field=DecimalField()))
    )['total'] or 0

    context = {
        'total_client': total_client,
        'total_client_h': total_client_h,
        'total_client_f': total_client_f,
        'total_commande_recue': total_commande_recue,
        'total_commande_livree': total_commande_livree,
        'total_revenus': total_revenus,
        'total_reste': total_reste,
    }

    return render(request, 'dashboard.html', context)


def deconnexion(request):
    logout(request)
    return redirect('login')