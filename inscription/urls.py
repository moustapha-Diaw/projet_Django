from django.urls import path, include
from inscription import views
from django.contrib import admin
from . import views


urlpatterns = [
    # path('admin/', admin.site.urls),
    path("dashboard/",views.dashboard, name="dashboard"),
    path("",views.home, name="index"),
    path('compte/',views.compte, name="compte"),
    path('connexion/',views.connexion, name="connexion"),
    path('inscription/',views.inscription, name="inscription"),
    path('paiement/',views.paiement, name="paiement"),
    path('faq/',views.faq, name="faq"),
    path('contact/',views.contact, name="contact"),
    path('inscription_reussie/', views.inscription_reussie, name='inscription_reussie'),
    
]
