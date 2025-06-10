from django import forms
from django.contrib.auth.forms import UserCreationForm

from page_p.models import RendezVous


class CustomUserCreationForm(UserCreationForm):
    
    password1 = forms.CharField(
        label="Password",
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
    )
    password2 = forms.CharField(
        label="Password confirmation",
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
        strip=False,
    )

    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ("password1", "password2")



class RendezVousForm(forms.ModelForm):
    class Meta:
        model = RendezVous
        fields = ['date_heure', 'motif', 'medecin', 'patient']
        widgets = {
            'medecin': forms.Select(attrs={'class': 'form-control'}),
            'patient': forms.Select(attrs={'class': 'form-control'}),
        }
        
        
