from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [

    path('login/', views.login, name='login'),
    path('check_login/', views.check_login, name='check_login'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('profile/create/', views.create_profile, name='create_profile'),
    path('check_register/', views.check_register, name='check_register'),
    path('verify-code/', views.verify_code, name='verify_code'),
    path('check_verify_code/', views.check_verify_code, name='check_verify_code'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
