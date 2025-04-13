from django.contrib import admin
from .models import FAQ
from .models import Inscription, Paiement, Contact, User

# @admin.register(Inscription)
class InscriptionAdmin(admin.ModelAdmin):
    list_display = ('nom', 'prenom', 'adresse', 'email', 'filiere', 'niveau', 'date_inscription')

class ContactAdmin(admin.ModelAdmin):
    list_display = ('nom', 'email', 'objet')

class FAQAdmin(admin.ModelAdmin):
    list_display = ('question', 'reponse')

# Enregistrer FAQ une seule fois
admin.site.register(FAQ, FAQAdmin)

# Enregistrer les autres modèles
admin.site.register(Inscription, InscriptionAdmin)
admin.site.register(Paiement)
admin.site.register(Contact, ContactAdmin)
admin.site.register(User)