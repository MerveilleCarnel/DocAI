from django.contrib import admin
from .models import Message, Patient, RendezVous , Room, Utilisateur
from .models import Medecin

# Register your models here.

admin.site.register(Utilisateur)
admin.site.register(Message)
admin.site.register(Room)
admin.site.register(RendezVous)
admin.site.register(Medecin)
admin.site.register(Patient) 