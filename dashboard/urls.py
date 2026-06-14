from django.urls import path
from django.contrib import admin
from django.contrib.auth import views as auth_views
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [

    path('', views.dashboard, name='dashboard'),
    path('deconnexion/', views.deconnexion, name='deconnexion'),
    path('modeles/', views.mes_modeles, name='modeles'),
    path('modeles/supprimer/<int:modele_id>/', views.supprimer_modele, name='supprimer_modele'),

    path('depenses/', views.depenses, name='depenses'),
    path('depenses/modifier/<int:pk>/', views.modifier_depense, name='modifier_depense'),
    path('depenses/supprimer/<int:pk>/', views.supprimer_depense, name='supprimer_depense'),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
