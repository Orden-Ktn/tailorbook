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
            code = user.generate_verification_code()
            
            # Rendu du template HTML
            html_content = render_to_string('email_code.html', {'user': user, 'code': code})
            
            # Création de l'email
            email = EmailMultiAlternatives(
                subject="Code de vérification",
                body=f"Votre code de vérification est : {code}", 
                from_email=settings.DEFAULT_FROM_EMAIL,
                to=[user.email],
            )
            email.attach_alternative(html_content, "text/html")  # ajoute la version HTML
            email.send(fail_silently=False)
            
            # Sauvegarde dans la session
            request.session['new_user_id'] = user.id
            messages.success(request, "Inscription réussie. Confirmez votre email en entrant le code envoyé.")
            return redirect('verify_code')
        else:
            messages.error(request, "Erreur lors de l'inscription.")
    else:
        form = CustomUserCreationForm()

    return render(request, 'register.html', {'form': form})


def verify_code(request):
    form = VerificationCodeForm()
    return render(request, 'verify_code.html',  {'form': form})


def check_verify_code(request):
    user_id = request.session.get('new_user_id')
    if not user_id:
        return redirect('register')

    user = get_object_or_404(CustomUser, id=user_id)

    if request.method == "POST":
        form = VerificationCodeForm(request.POST)
        if form.is_valid():
            code = form.cleaned_data['code']
            if code == user.verification_code:
                user.is_email_verified = True
                user.verification_code = ''
                user.save()
                messages.success(request, "Email vérifié ! Complétez votre profil.")
                return redirect('profile')
            else:
                messages.error(request, "Code incorrect. Essayez encore.")
    else:
        form = VerificationCodeForm()

    return render(request, 'verify_code.html', {'form': form})


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
        email = form.cleaned_data['email']
        password = form.cleaned_data['password']

        user = authenticate(request, email=email, password=password)

        if user is not None:
            auth_login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, "Email ou mot de passe incorrect")

    return render(request, 'login.html', {'form': form})
