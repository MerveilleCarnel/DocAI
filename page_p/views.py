import os
from urllib import request
from django.db import IntegrityError
import openai
from http import client
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm 
from .form import CustomUserCreationForm,  RendezVousForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from openai import OpenAI
from django.http import HttpResponse, JsonResponse
from django.views.decorators.http import require_POST
from .models import RendezVous

from django.core.exceptions import ValidationError
import json

# Create your views here.
from django.views.generic import TemplateView

class HomePageView(TemplateView):
    template_name = "home.html"
    
class GeneralistePageView(TemplateView):
    template_name = "generaliste.html"
    
class SpecialistePageView(TemplateView):
    template_name = "specialiste.html"  
    
class Specialiste1PageView(TemplateView):
    template_name = "specialiste1.html"  
    
class Specialiste2PageView(TemplateView):
    template_name = "specialiste2.html"  
    
class OrlPageView(TemplateView):
    template_name = "orl.html"   
    
class PediatrePageView(TemplateView):
    template_name = "pediatre.html"                
    
class Medecin1PageView(TemplateView):
    template_name = "medecin1.html" 
    
class Medecin2PageView(TemplateView):
    template_name = "medecin2.html"            
    
class ProfilPageView(TemplateView):
    template_name = "profil.html"  
    
class MedecinPageView(TemplateView):
    template_name = "medecin.html"        
 
class AboutPageView(TemplateView):
    template_name = "about.html"
    
class ContactPageView(TemplateView):
        template_name = "contact.html"
        
class ParametrePageView(TemplateView):
        template_name = "parametre.html"  
class ChatbotPageView(TemplateView):
        template_name = "chatbot.html"
class DossiermedicalPageView(TemplateView):
        template_name = "dossier_medical.html"         
           
class ConsulterPageView(TemplateView):
        template_name = "consulter.html"         
                                         
class AccesrefusePageView(TemplateView):
        template_name = "acces_refuse.html"  

      
def inscription(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('connexion')
    else:
        form = CustomUserCreationForm()
    return render(request, 'inscription.html', {'form': form})

from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login

def connexion(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)

            if user.username == "DEMGNE":
                return redirect('medecin')
            else:
                return redirect('chatbot')
        else:
            messages.error(request, 'Nom d\'utilisateur ou mot de passe incorrect.')
    else:
        return render(request, 'connexion.html')

@login_required
def home(request):
    user = user.objects.get(username=request.user.username)  # Récupérer l'utilisateur connecté
    return render(request, 'chatbot.html', {'user': user})


def deconnexion(request):
    logout(request)
    return redirect('connexion')


@require_POST
def consultation(request):
    client = openai.OpenAI()
    openai.api_key == os.getenv ('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')
 
    conversation = [  # Initial conversation
        {"role": "user", "content": "tu es un medecin expérimenter"},
        {"role": "user", "content": "bonjour docteur je ne me sent pas bien"}
    ]

    conversation = request.session.get('conversation', conversation)  # Use session or default to initial
    
    
    if request.method == "POST":
        user_input= request.POST.get('user_input')
        conversation.append({"role":"user","content":user_input})
        
        response=client.chat.completions.create(
            model="gpt-4o",
            messages= conversation
        ).choices[0].message.content
        conversation.append({"role":"assistant","content":response}) 
        request.session['conversation'] = conversation
    context={'conversation':conversation}  
    return render(request, 'chatbot.html', context)  


def rendezvous(request):
  if request.method == 'POST':
    form = RendezVousForm(request.POST)
    if form.is_valid():
      rendez_vous = form.save()
      # On récupère l'objet créé (rendez_vous)
      
      return redirect('confirmation_rendez_vous', rendez_vous_id=rendez_vous.id)  # Rediriger avec le contexte
    else:
      return render(request, 'rendezvous.html', {'form': form})
  else:
    form = RendezVousForm()
  return render(request, 'rendezvous.html', {'form': form})


def confirmation_rendez_vous(request, rendez_vous_id):
    try:
        rendez_vous = RendezVous.objects.get(pk=rendez_vous_id)
        context = {'rendez_vous': rendez_vous}
    except RendezVous.DoesNotExist:
        
        return render(request, 'erreur_404.html', status=404)
    return render(request, 'confirmation_rendez_vous.html', context)


def modifier_rendez_vous(request, rendez_vous_id):
    try:
        rendez_vous = RendezVous.objects.get(pk=rendez_vous_id)
    except RendezVous.DoesNotExist:
        # Gérer le cas où le rendez-vous n'existe pas
        return render(request, 'erreur_404.html', status=404)

    if request.method == 'POST':
        form = RendezVousForm(request.POST, instance=rendez_vous)
        if form.is_valid():
            form.save()
            return redirect('confirmation_rendez_vous', rendez_vous_id=rendez_vous.id)
        else:
            # Afficher les erreurs du formulaire
            context = {'form': form, 'rendez_vous': rendez_vous, 'errors': form.errors}
            return render(request, 'modifier_rendez_vous.html', context)
    else:
        form = RendezVousForm(instance=rendez_vous)
    return render(request, 'modifier_rendez_vous.html', {'form': form, 'rendez_vous': rendez_vous})


def annuler_rendez_vous(request, rendez_vous_id):
    rendez_vous = RendezVous.objects.get(pk=rendez_vous_id)
    rendez_vous.annule = True
    rendez_vous.save()
    return redirect('medecin')  


def visualiser(request):
    rendez_vous = RendezVous.objects.all()
    return render(request, 'visualiser.html', {'rendez_vous': rendez_vous})