from django.urls import path
from magasin.views import index, detail, checkout, confimation
from django.urls import path, include
from . import views
from .views import CategoryAPIView
from django.conf import settings
from .views import ProductAPIView
from django.urls import path, include
from django.contrib.auth import views as auth_views  # Correct import statement

from django.conf.urls.static import static # Correct import statement

#import re
from .views import index
from django.urls import path
from django.contrib.auth import views as auth_views
from .views import ProductViewset
from .views import CategoryAPIView

#router = routers.DefaultRouter()
#router.register(r'products', ProductViewset)
urlpatterns = [
    

    #path('', index, name='index'),
    path('api/category/', CategoryAPIView.as_view()), 
    path('api/produits/', ProductAPIView.as_view()), 
    #path('home/', views.home, name='home'),

    #path('creer_commande/', views.creer_commande, name='creer_commande'),
    path('ajouter_produit/', views.ajouter_produit, name='ajouter_produit'),
    #path('affiche_commande/<int:commande_id>/',views.affiche_commande, name='affiche_commande'),
    path('lprod/', views.lprod, name='lprod'),
    path('majProduits/', views.majProduits, name='majProduits'),

    path('', index, name='home'),
    path('Lfournisseur/', views.Lfournisseur, name='Lfournisseur'),
    path('Lfournisseur/<str:nom>/', views.Lfournisseur, name='Lfournisseur'),
    path('addfournisseur/', views.addfournisseur,name='addfournisseur'),
    path('Lfournisseur/deletefournisseur/<str:nom>/', views.deletefournisseur,name='deletefournisseur'),
    path('Lfournisseur/updatefournisseur/<str:nom>/', views.updatefournisseur, name='updatefournisseur'),
    
    path('addcategorie/', views.addcategorie, name='addcategorie'),
    path('categorie_list/', views.categorie_list, name='categorie_list'),
    path('categorie_detail/<int:categorie_id>/', views.categorie_detail, name='categorie_detail'),
    path('categorie_list/deletecategorie/<str:name>/', views.deletecategorie,name='deletecategorie'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html', success_url='index'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='registration/logout.html'), name='logout'),
    path('<int:myid>', detail, name="detail"),
    path('checkout', checkout, name="checkout"),
    path("majProduits/", views.produit, name="produit"),
    #path('fournisseur/', views.fournisseur, name='fournisseur'), 
    path('confirmation', confimation, name="confirmation" ),
]

