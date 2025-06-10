from django.db import models
from datetime import datetime

from django.contrib.auth.models import AbstractUser

# Create your models here.
class Utilisateur(models.Model):
    username = models.CharField(max_length=50)  
    password= models.CharField(max_length=50)
    sexe = models.CharField(max_length=1, choices=[('M', 'Masculin'), ('F', 'Féminin'), ('X', 'Non-spécifié')], default='X')
    
class Room(models.Model):
    name = models.CharField(max_length=2000)

class Message(models.Model):
    value = models.CharField(max_length=1000000)
    date = models.DateTimeField(default=datetime.now , blank = True)
    user = models.CharField(max_length=1000000)
    room = models.CharField(max_length=1000000)
    


class Medecin(models.Model):
    numero_ordre = models.PositiveIntegerField(unique=True)
    specialite = models.CharField(max_length=100)
    service_organisation = models.CharField(max_length=255)
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)

    def __str__(self):
        return f"Dr. {self.nom} {self.prenom} ({self.specialite})"


class Patient(AbstractUser):
    # Champs supplémentaires si nécessaire (par exemple, date de naissance, numéro de sécurité sociale, etc.)
    date_naissance = models.DateField(null=True, blank=True)
    
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='patients',
        blank=True,
        help_text='The groups this user belongs to. A user can belong to multiple groups.'
    )

    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='patients',
        blank=True,
        help_text='Specific permissions for this user.'
    )
   
    def __str__(self):
        return f"{self.username}"

class RendezVous(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, null=True, blank=True)
    medecin = models.ForeignKey(Medecin, on_delete=models.CASCADE, null=True, blank=True)  # Autorise les valeurs nulles
    date_heure = models.DateTimeField()
    motif = models.TextField()
    annule = models.BooleanField(default=False, verbose_name="Annulé")

    STATUTS = [
        ('confirmé', 'Confirmé'),
        ('annulé', 'Annulé'),
        ('reporté', 'Reporté'),
    ]
    statut = models.CharField(max_length=10, choices=STATUTS, default='confirmé')

    

    