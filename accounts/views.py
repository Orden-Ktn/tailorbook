from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.models import User
from django.contrib.auth import login as auth_login, authenticate, logout, update_session_auth_hash, get_user_model
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail, EmailMultiAlternatives
from django.template.loader import render_to_string

User = get_user_model()


def register(request):
    form = CustomUserCreationForm()
    return render(request, 'register.html',  {'form': form})


def check_register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            
            # Sauvegarde dans la session
            request.session['new_user_id'] = user.id
            messages.success(request, "Inscription réussie ! Complétez votre profil.")
            return redirect('profile')
        else:
            messages.error(request, "Erreur lors de l'inscription.")
    else:
        form = CustomUserCreationForm()

    return render(request, 'register.html', {'form': form})


def profile(request):
    form = ProfileForm()
    return render(request, 'profile.html',  {'form': form})


def create_profile(request):
    user_id = request.session.get('new_user_id')

    if not user_id:
        return redirect('register')

    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user_id = user_id
            profile.save()

            del request.session['new_user_id']
            messages.success(request, "Profil créé avec succès. Connectez-vous.")
            return redirect('login')
    else:
        form = ProfileForm()

    return render(request, 'profile.html', {'form': form})


def login(request):
    form = LoginForm()
    return render(request, 'login.html',  {'form': form})


def check_login(request):
    form = LoginForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth_login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, "Nom d'utilisateur ou mot de passe incorrect")

    return render(request, 'login.html', {'form': form})