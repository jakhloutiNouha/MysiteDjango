from django.shortcuts import redirect, render
from .models import Product, Commande
from django.core.paginator import Paginator
from .models import Fournisseur
from .models import Category 
from .serializers import CategorySerializer
#from .serializers import ProductSerializer
from rest_framework import viewsets  # Importez directement CategorySerializer
from .serializers import ProductSerializer  # Importez directement ProductSerializer
from .forms import FournisseurForm 
from .forms import CategorieForm
from rest_framework.views import APIView
from django.http import HttpResponseRedirect  # Importez HttpResponseRedirect depuis django.http
from django.urls import reverse
from django.shortcuts import redirect, render
from decimal import Decimal
from .forms import ProduitForm
from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegistrationForm
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth import logout

import re  # Module pour les expressions régulières
from rest_framework.response import Response



def index(request):
    # Your view logic here
    return render(request, 'magasin/index.html')

#from .forms import ProduitForm
def logout_view(request):
    logout(request)
    # Rediriger vers la page de connexion ou une autre page spécifiée après la déconnexion
    return redirect('login')  # Assurez-vous de remplacer 'login' par le nom de l'URL de la page de connexion

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, f'Bienvenue {username}, votre compte a été créé avec succès !')
            return redirect('index')
    else:
        form = UserRegistrationForm()
    return render(request, 'registration/register.html', {'form': form})


def addcategorie(request):
    context = {}
    if request.method == "POST":
        form = CategorieForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('magasin:categorie_list')
    else:
        form = CategorieForm()
        context.update({'form': form})
    return render(request, 'magasin/majcategorie.html', context)



class CategoryAPIView(APIView):
    def get(self, request, *args, **kwargs):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)

def deletecategorie(request, name):
    categories = Category.objects.filter(name=name)
    categories.delete()
    return redirect('magasin:categorie_list')




def categorie_list(request):
    categories = Category.objects.all()  # Récupérer toutes les catégories
    return render(request, 'magasin/categorie_list.html', {'categories': categories})
def categorie_detail(request, categorie_id):
    categorie = Category.objects.get(id=categorie_id)
    produits = categorie.produit_set.all()
    context = {
        'categorie': categorie,
        'produits': produits,
    }
    return render(request, 'magasin/categorie_detail.html', context)

# Create your views here.
def index(request):
    product_object = Product.objects.all()
    item_name = request.GET.get('item-name')
    if item_name !='' and item_name is not None:
        product_object = Product.objects.filter(title__icontains=item_name)
    paginator = Paginator(product_object, 4)
    page = request.GET.get('page')
    product_object = paginator.get_page(page)
    return render(request, 'magasin/index.html', {'product_object': product_object})

def detail(request, myid):
    product_object = Product.objects.get(id=myid)
    return render(request, 'magasin/detail.html', {'product': product_object}) 


def checkout(request):
    if request.method == "POST":
        items = request.POST.get('items')
        total_str = request.POST.get('total')
        total_cleaned = ''.join(c for c in total_str if c.isdigit() or c == '.')
        try:
            total = Decimal(total_cleaned)
        except DecimalInvalidOperation:
            total = Decimal('0.0')  

        nom = request.POST.get('nom')
        email = request.POST.get('email')
        address = request.POST.get('address')
        ville = request.POST.get('ville')
        
        
        com = Commande(
            items=items,
            total=total,
            nom=nom,
            email=email,
            address=address,
            ville=ville
        )
        com.save()
        return redirect('confirmation')

    return render(request, 'magasin/checkout.html')

from django.shortcuts import render, get_object_or_404
from .models import Category

def categorie_detail(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    produits = category.produit_set.all()  # Check this line
    return render(request, 'categorie_detail.html', {'category': category, 'produits': produits})



def updatefournisseur(request,nom):  
    fournisseur = get_object_or_404(Fournisseur,nom=nom) 
    if request.method == 'POST':
        form = FournisseurForm(request.POST, instance=fournisseur) 
        if form.is_valid():
            form.save()
            return redirect(reverse('magasin:Lfournisseur'))
    else:
        form = FournisseurForm(instance=fournisseur)
    context = {'form': form, 'fournisseur': fournisseur}        
    return render(request,'magasin/updatefournisseur.html',context)
 # Assurez-vous d'importer le formulaire FournisseurForm correctement

def addfournisseur(request):
    context = {}  # Initialisez context en dehors de la logique conditionnelle

    if request.method == 'POST':
        form = FournisseurForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('magasin:Lfournisseur')
            except:
                pass
    else:
        form = FournisseurForm()
    
    context['form'] = form  # Ajoutez le formulaire au contexte dans tous les cas

    return render(request, 'magasin/addfournisseur.html', context)
def detailProduit(request,description):
    product = Product.objects.get(description=description) 
    return render(request,'magasin/detailProduit.html', context={'product':product})  
def lprod(request):
    product =Product.objects.all()
    context={'product':product}
    return render(request,'magasin/lprod.html',{'product':product})
def majProduits(request):
    context = {}
    if request.method == 'POST':
        form = ProduitForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                form.save()
                return redirect('magasin:lprod')
            except:
                pass
    else:
        form = ProduitForm()
        context.update({'form': form}) 
    return render(request, 'magasin/majproduits.html', context)
def deleteProduit(request,description): 
    try:
        form = Produit.objects.get(description=description)  
        form.delete()
    except Fournisseur.MultipleObjectsReturned:
        fournisseurs = Fournisseur.objects.filter(name=name)
    except Fournisseur.DoesNotExist:
        pass
    return redirect('magasin:catalogue')
class ProductAPIView(APIView):
    def get(self, *args, **kwargs):
        produits = Product.objects.all()
        serializer = ProductSerializer(produits, many=True)
        return Response(serializer.data)

class ProductViewset(viewsets.ReadOnlyModelViewSet):
    serializer_class = ProductSerializer
    def get_queryset(self):
        queryset = Product.objects.filter()#active=True
        category_id = self.request.GET.get('category_id')
        if category_id:
            queryset = queryset.filter(categorie_id=category_id)
        return queryset

def ajouter_produit(request):
    if request.method == 'POST':
        form = AjouterProduitForm(request.POST)
        if form.is_valid():
            produit_id = form.cleaned_data['produit'].id
            quantite = form.cleaned_data['quantite']
            produit = Produit.objects.get(pk=produit_id)
            
    else:
        form = AjouterProduitForm()
    return render(request, 'magasin/ajouter_produit.html', {'form': form})
 
def Lfournisseur(request):
    fournisseur = Fournisseur.objects.all()
    context={'fournisseur':fournisseur}
    return render( request,'magasin/Lfournisseur.html',context )

def deletefournisseur(request,nom): 
    fournisseur = Fournisseur.objects.get(nom=nom)  
    fournisseur.delete()
    return redirect('magasin:Lfournisseur')

def produit(request):
    if request.method == "POST":
        form = ProduitForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/")
    else:
        form = ProduitForm()
    return render(request, "magasin/majProduits.html", {"form": form})
def confimation(request):
    info = Commande.objects.all()[:1]
    for item in info:
        nom = item.nom
    return render(request, 'magasin/confirmation.html', {'name': nom})          