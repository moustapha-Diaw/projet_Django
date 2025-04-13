from django import forms
from .models import Inscription
from .models import Contact
from .models import User




# Formulaire inscription
class InscriptionForm(forms.ModelForm):
    class Meta:
        model = Inscription
        fields = ['nom', 'prenom', 'adresse', 'email', 'filiere', 'niveau', 'date_naissance', 'photo', 'type_document', 'fichier']
        widgets = {
            'date_naissance': forms.DateInput(attrs={'type': 'date'})  # Permet de choisir une date avec un sélecteur
        }

# Formulaire contact
class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['nom', 'email', 'objet', 'message']



# Formulaire User
class CompteForm(forms.Form):
    username = forms.CharField(label="Nom d'utilisateur", widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label="Mot de passe", widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    role = forms.ChoiceField(
        label="Rôle",
        choices=[
            ('admin', 'Administrateur'),
            ('agent', 'Agent'),
        ],
        widget=forms.Select(attrs={'class': 'form-control'})
    )
