from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

@login_required
def client(request):
    form = ClientForm(user=request.user)
    client = Client.objects.filter(atelier=request.user).order_by('-id') 
    # Pagination - 10 éléments par page
    paginator = Paginator(client, 10)
    page = request.GET.get('page')
    
    try:
        clients = paginator.page(page)
    except PageNotAnInteger:
        clients = paginator.page(1)
    except EmptyPage:
        clients = paginator.page(paginator.num_pages)

    return render(request, 'client.html', {
        "form": form,
        'client': clients
    })


@login_required
def ajouter_client(request):
    if request.method == "POST":
        client_id = request.POST.get("client_id")

        # MODIFICATION
        if client_id:
            client = get_object_or_404(Client, id=client_id)
            form = ClientForm(request.POST, instance=client, user=request.user)

            if form.is_valid():
                form.save()
                messages.success(request, "Client(e) modifié(e) avec succès !")
                return redirect("client")
            else:
                print(form.errors)

        # AJOUT
        else:
            form = ClientForm(request.POST, user=request.user)

            if form.is_valid():
                client = form.save(commit=False)
                client.atelier = request.user
                client.save()
                messages.success(request, "Client(e) enregistré(e) !")
                return redirect("client")
            else:
                print(form.errors)

    else:
        form = ClientForm(user=request.user)

    return render(request, "client.html", {"form": form})




@login_required
def supprimer_client(request, client_id):
    client = get_object_or_404(Client, id=client_id)
    client.delete()
    messages.success(request, "Client(e) supprimé(e) avec succès.")
    return redirect('client')


@login_required
def mesures_femmes(request):
    # Récupérer tous les mesures pour la liste
    mesures = MesureFemme.objects.filter(client__atelier=request.user).order_by('-date')

    # Clients qui n'ont pas encore de mesure
    clients_mesures = MesureFemme.objects.filter(client__atelier=request.user).values_list('client_id', flat=True)
    clients_disponibles = Client.objects.filter(atelier=request.user, sexe="F").exclude(id__in=clients_mesures)

    # Formulaire avec le queryset filtré
    form = MesureFemmeForm(user=request.user)
    form.fields['client'].queryset = clients_disponibles

    # Pagination
    paginator = Paginator(mesures, 10)
    page = request.GET.get('page')
    try:
        mesures_page = paginator.page(page)
    except PageNotAnInteger:
        mesures_page = paginator.page(1)
    except EmptyPage:
        mesures_page = paginator.page(paginator.num_pages)

    return render(request, 'mesure_femme.html', {
        "form": form,
        "mesures": mesures_page,
        "client": clients_disponibles
    })


@login_required
def ajouter_mesure_femme(request):
    if request.method == "POST":
        form = MesureFemmeForm(request.POST, user=request.user)
        if form.is_valid():
            client = form.cleaned_data['client']

            # Vérifier si une mesure existe déjà pour ce client
            if MesureFemme.objects.filter(client=client).exists():
                messages.error(request, "Cette cliente possède déjà des mesures.")
                return redirect("mesures_femmes")
            else:
                form.save()
                messages.success(request, "Mesure enregistrée pour cette cliente.")
                return redirect('mesures_femmes')
    else:
        form = MesureFemmeForm(user=request.user)

    return render(request, 'mesure_femme.html', {"form": form})


def modifier_mesure_femme(request, mesure_id):
    mesure = get_object_or_404(MesureFemme, id=mesure_id)
    if request.method == 'POST':
        form = MesureFemmeForm(request.POST, instance=mesure)
        if form.is_valid():
            form.save()
            messages.success(request, "Mesure modifiée avec succès.")
        else:
            messages.error(request, "Echec de la modification.")
    return redirect('mesures_femmes')


@login_required
def supprimer_mesure_femme(request, id):
    mesurefemme = get_object_or_404(MesureFemme, id=id)
    mesurefemme.delete()
    messages.success(request, "Mesure supprimée avec succès.")
    return redirect('mesures_femmes')




@login_required
def mesures_hommes(request):
    # Récupérer tous les mesures pour la liste
    mesures = MesureHomme.objects.filter(client__atelier=request.user).order_by('-date')

    # Clients qui n'ont pas encore de mesure
    clients_mesures = MesureHomme.objects.filter(client__atelier=request.user).values_list('client_id', flat=True)
    clients_disponibles = Client.objects.filter(atelier=request.user, sexe="M").exclude(id__in=clients_mesures)

    # Formulaire avec le queryset filtré
    form = MesureHommeForm(user=request.user)
    form.fields['client'].queryset = clients_disponibles

    # Pagination
    paginator = Paginator(mesures, 10)
    page = request.GET.get('page')
    try:
        mesures_page = paginator.page(page)
    except PageNotAnInteger:
        mesures_page = paginator.page(1)
    except EmptyPage:
        mesures_page = paginator.page(paginator.num_pages)

    return render(request, 'mesure_homme.html', {
        "form": form,
        "mesures": mesures_page,
        "client": clients_disponibles
    })


@login_required
def ajouter_mesure_homme(request):
    if request.method == "POST":
        form = MesureHommeForm(request.POST, user=request.user)
        if form.is_valid():
            client = form.cleaned_data['client']

            # Vérifier si une mesure existe déjà pour ce client
            if MesureHomme.objects.filter(client=client).exists():
                messages.error(request, "Ce client possède déjà des mesures.")
                return redirect("mesures_hommes")
            else:
                form.save()
                messages.success(request, "Mesure enregistrée pour ce client.")
                return redirect('mesures_hommes')
    else:
        form = MesureHommeForm(user=request.user)

    return render(request, 'mesure_homme.html', {"form": form})


def modifier_mesure_homme(request, mesure_id):
    mesure = get_object_or_404(MesureHomme, id=mesure_id)
    if request.method == 'POST':
        form = MesureHommeForm(request.POST, instance=mesure)
        if form.is_valid():
            form.save()
            messages.success(request, "Mesure modifiée avec succès.")
        else:
            messages.error(request, "Echec de la modification.")
    return redirect('mesures_hommes')


@login_required
def supprimer_mesure_homme(request, id):
    mesurehomme = get_object_or_404(MesureHomme, id=id)
    mesurehomme.delete()
    messages.success(request, "Mesure supprimée avec succès.")
    return redirect('mesures_hommes')


