from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [

    path('', views.accueil, name='accueil'),
    path('galerie/', views.galerie_tailleurs, name='galerie_tailleurs'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
