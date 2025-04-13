from django.db import models
from django.contrib.auth.models import User



# Create your models here.
class User(models.Model):
    ROLE_CHOICES = [('admin', 'Admin'), ('agent', 'Agent')]
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    mot_de_passe = models.TextField()
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    date_creation = models.DateTimeField(auto_now_add=True)


    

class Inscription(models.Model):
    FILIERE_CHOICES = [('IG', 'Informatique de Gestion'), ('ELM', 'Électro-mecanique'), ('AD', 'Administration')]
    NIVEAU_CHOICES = [('AP', 'Année Préparatoire'), ('L1', 'Licence 1'), ('L2', 'Licence 2'), ('L3', 'Licence 3')]

    nom = models.CharField(max_length=100, default='')  # Valeur par défaut vide
    prenom = models.CharField(max_length=100, default='')  # Valeur par défaut vide
    adresse = models.CharField(max_length=100, default='')  # Valeur par défaut vide
    email = models.EmailField(unique=True, default='')  # Valeur par défaut vide
    filiere = models.CharField(max_length=50, choices=FILIERE_CHOICES, default='IG')  # Valeur par défaut 'Informatique de Gestion'
    niveau = models.CharField(max_length=50, choices=NIVEAU_CHOICES, default='L1')  # Valeur par défaut 'Licence 1'
    date_naissance = models.DateField(null=True, blank=True)  # Valeur par défaut None (null)
    photo = models.ImageField(upload_to='photos/', null=True, blank=True)  # Valeur par défaut None (null)
    type_document = models.CharField(max_length=100, default='inconnu')  # Valeur par défaut 'inconnu'
    fichier = models.ImageField(upload_to='photos/', null=True, blank=True)  # Valeur par défaut None (null)
    statut_inscription = models.CharField(max_length=50, choices=[('en attente', 'En attente'), ('validée', 'Validée'), ('rejetée', 'Rejetée')], default='en attente')  # Valeur par défaut 'en attente'
    date_inscription = models.DateTimeField(auto_now_add=True)  # Valeur par défaut l'heure actuelle au moment de l'ajout

class Paiement(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    montant = models.DecimalField(max_digits=10, decimal_places=2)
    methode = models.CharField(max_length=50, choices=[('espèces', 'Espèces'), ('mobile money', 'Mobile Money'), ('virement', 'Virement')])
    statut = models.CharField(max_length=50, choices=[('en attente', 'En attente'), ('effectué', 'Effectué')], default='en attente')
    date_paiement = models.DateTimeField(auto_now_add=True)

class FAQ(models.Model):
    question = models.TextField(max_length=255)
    reponse = models.TextField()
    date_creation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.question
class Contact(models.Model):
    nom = models.CharField(max_length=255)
    email = models.EmailField()
    objet = models.CharField(max_length=255)
    message = models.TextField()
    date_envoi = models.DateTimeField(auto_now_add=True)







