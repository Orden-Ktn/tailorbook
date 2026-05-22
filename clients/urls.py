from django.urls import path
from . import views

urlpatterns = [
    path("", views.client, name="client"),
    path("ajouter/", views.ajouter_client, name="ajouter_client"),
    path('supprimer/<int:client_id>/', views.supprimer_client, name='supprimer_client'),

    path("mesures_femmes/", views.mesures_femmes, name="mesures_femmes"),
    path("mesure_femme/", views.ajouter_mesure_femme, name="ajouter_mesure_femme"),
    path('mesures_femmes/<int:mesure_id>/modifier/', views.modifier_mesure_femme, name='modifier_mesure_femme'),
    path('mesures_femmes/supprimer/<int:id>/', views.supprimer_mesure_femme, name='supprimer_mesure_femme'),


    path("mesures_hommes/", views.mesures_hommes, name="mesures_hommes"),
    path("mesure_homme/", views.ajouter_mesure_homme, name="ajouter_mesure_homme"),
    path('mesures_hommes/<int:mesure_id>/modifier/', views.modifier_mesure_homme, name='modifier_mesure_homme'),
    path('mesures_hommes/supprimer/<int:id>/', views.supprimer_mesure_homme, name='supprimer_mesure_homme'),

    
]
