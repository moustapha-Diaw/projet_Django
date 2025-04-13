from django.shortcuts import render, redirect
from .models import Inscription
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import InscriptionForm
from .forms import CompteForm
from .forms import ContactForm
from django.contrib import messages
from .models import FAQ



# Create your views here.
def dashboard(request, *args, **kwargs):
    return render(request, 'dashboard.html')


def home(request):
    return render(request, "index.html")


def inscription(request):

    return render(request, "inscription.html",)

def paiement(request):
    return render(request, "paiement.html")

def faq(request):
    return render(request, "faq.html")

from .models import FAQ

def faq(request):
    faqs = FAQ.objects.all()
    return render(request, 'faq.html', {'faqs': faqs})


def contact(request):
    return render(request, "contact.html")

def inscription_reussie(request):
    return render(request, 'inscription_reussie.html')


# def compte(request):
#     return render(request, "compte.html")


def compte(request):
    return render(request, "compte.html")

def connexion(request):
    return render(request, "connexion.html")


@login_required
def admin(request):
    return render(request, "admin.html")



# Inscription
def inscription(request):
    if request.method == 'POST':
        form = InscriptionForm(request.POST)
        
        if form.is_valid():
            form.save()  # Enregistre l'Inscription dans la base de données
            return redirect('inscription_reussie')  # Redirige vers une page de confirmation
    else:
        form = InscriptionForm()
    return render(request, 'inscription.html', {'form': form})


# Compte

def compte(request):
    if request.method == 'POST':
        form = CompteForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            role = form.cleaned_data['role']

            try:
                user = CustomUser.objects.get(username=username)
            except CustomUser.DoesNotExist:
                form.add_error('username', "Nom d'utilisateur inexistant.")
                return render(request, 'compte.html', {'form': form})

            # Vérifier le mot de passe
            if not user.check_password(password):
                form.add_error('password', "Mot de passe incorrect.")
                return render(request, 'compte.html', {'form': form})

            # Vérifier le rôle
            if user.role != role:
                form.add_error('role', "Le rôle ne correspond pas à cet utilisateur.")
                return render(request, 'compte.html', {'form': form})

            # Authentifier et connecter l'utilisateur
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard')  # Redirection vers le tableau de bord
            else:
                form.add_error(None, "Erreur lors de l'authentification.")
    else:
        form = CompteForm()

    return render(request, 'compte.html', {'form': form})



#  Contact
def contact(request):
    form = ContactForm()

    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            # Afficher un message de succès
            messages.success(request, "Votre message a bien été envoyé !")
            # Réinitialiser le formulaire après soumission
            form = ContactForm()
        else:
            # Afficher un message d'erreur si le formulaire n'est pas valide
            messages.error(request, "Il y a eu une erreur dans l'envoi de votre message. Veuillez réessayer.")

    # Retourner la page avec le formulaire et les messages (affichés seulement après soumission)
    return render(request, "contact.html", {"form": form})
