
from django.urls import path

from django.contrib import admin
from .views import AccesrefusePageView, ChatbotPageView, ConsulterPageView, DossiermedicalPageView, HomePageView,  OrlPageView, PediatrePageView, Specialiste1PageView, Specialiste2PageView, SpecialistePageView, AboutPageView,Medecin1PageView,Medecin2PageView, ContactPageView, MedecinPageView, ProfilPageView,GeneralistePageView, annuler_rendez_vous, confirmation_rendez_vous, inscription, connexion, deconnexion, ParametrePageView, consultation, MedecinPageView,  modifier_rendez_vous, rendezvous, visualiser

urlpatterns = [
     path('admin/', admin.site.urls),
    path("home/", HomePageView.as_view(), name="home"),
    path("about/", AboutPageView.as_view(), name="about"),
    path("contact/", ContactPageView.as_view(), name="contact"),
    path("parametre/", ParametrePageView.as_view(), name="parametre"),
    path('deconnexion/', deconnexion, name='deconnexion'),
    path("", inscription, name='inscription'),
    path("connexion/", connexion, name='connexion'),
    path("consultation/", consultation, name='consultation'),
    path("chatbot/", ChatbotPageView.as_view(), name='chatbot'),
    path("profil/", ProfilPageView.as_view(), name='profil'),
    path("medecin/", MedecinPageView.as_view(), name='medecin'),
    path("generaliste/", GeneralistePageView.as_view(), name='generaliste'),
    path("medecin1/", Medecin1PageView.as_view(), name='medecin1'),
    path("medecin2/", Medecin2PageView.as_view(), name='medecin2'),
    path("specialiste/", SpecialistePageView.as_view(), name='specialiste'),
    path("specialiste1/", Specialiste1PageView.as_view(), name='specialiste1'),
    path("specialiste2/", Specialiste2PageView.as_view(), name='specialiste2'),
    path("orl/", OrlPageView.as_view(), name='orl'),
    path("pediatre/", PediatrePageView.as_view(), name='pediatre'),
    path("rendezvous/", rendezvous , name='rendezvous'),
    path("confirmation_rendez_vous/<int:rendez_vous_id>/", confirmation_rendez_vous, name='confirmation_rendez_vous'),
    path("modifier_rendez_vous/<int:rendez_vous_id>/", modifier_rendez_vous, name='modifier_rendez_vous'),
    path("annuler_rendez_vous/<int:rendez_vous_id>/", annuler_rendez_vous, name='annuler_rendez_vous'),
    path('dossier_medical/', DossiermedicalPageView.as_view(), name='dossier_medical'),
    path('consulter/', ConsulterPageView.as_view(), name='consulter'),
    path('visualiser/',visualiser, name='visualiser'),
    path('acces_refuse/',AccesrefusePageView.as_view(), name='acces_refuse'),
   
    
]   
 