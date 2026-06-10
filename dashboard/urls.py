from django.urls import path
from django.contrib import admin
from django.contrib.auth import views as auth_views
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [

    path('', views.dashboard, name='dashboard'),
    path('deconnexion/', views.deconnexion, name='deconnexion'),
    path('mes-modeles/', views.mes_modeles, name='mes_modeles'),
    path('mes-modeles/supprimer/<int:modele_id>/', views.supprimer_modele, name='supprimer_modele'),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
