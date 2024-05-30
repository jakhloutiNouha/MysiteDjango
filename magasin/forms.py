from django.forms import ModelForm
from .models import Product, Fournisseur, Commande
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from .models import Category
from django import forms
from .models import Product  # Assurez-vous d'importer le modèle Produit
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(label='Prénom')
    last_name = forms.CharField(label='Nom')
    email = forms.EmailField(label='Adresse e-mail')

    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ('first_name', 'last_name', 'email')


class ProduitForm(forms.ModelForm):
    class Meta:
        model = Product  # Specify the relevant model
        fields = '__all__'  # Or specify specific fields that the form should include

class CategorieForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']

class FournisseurForm(ModelForm):
    class Meta:
        model = Fournisseur
        fields = "__all__"


class CommandeForm(ModelForm):
    class Meta:
        model = Commande
        fields = "__all__"
