from django.conf import settings
from django.urls import path
from . import views
from django.contrib import admin
from django.conf.urls.static import static



urlpatterns = [
    path("", views.commande, name="commande"),
    path("ajouter/", views.ajouter_commande, name="ajouter_commande"),
    path('supprimer/<int:commande_id>/', views.supprimer_commande, name='supprimer_commande'),
    path('terminer/<int:commande_id>/', views.terminer_commande, name='terminer_commande'),
    path('depense/<int:commande_id>/', views.ajouter_depense, name='ajouter_depense'),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
