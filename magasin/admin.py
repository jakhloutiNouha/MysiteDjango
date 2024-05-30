from django.contrib import admin
from .models import Category, Product, Commande, Fournisseur,ProduitNC

# Register your models here.
admin.site.site_header = "mysiteDjango"
admin.site.site_title = "SBC magasin"
admin.site.index_title = "Manager"


class AdminCategory(admin.ModelAdmin):
    list_display = ['name']  # Ajoutez d'autres champs si nécessaire

admin.site.register(Category, AdminCategory)
admin.site.register(ProduitNC)

class AdminProduct(admin.ModelAdmin):
    list_display = ('title', 'price', 'category', 'date_added')
    search_fields = ('title',)
    list_editable = ('price',)

class AdminCommande(admin.ModelAdmin):
    # Address 'items' field (consider ManyToManyField or a descriptive field)
    list_display = ('nom', 'email', 'address', 'ville', 'pays', 'total', 'date_commande')  # Update field types for total and zipcode later

class AdminFournisseur(admin.ModelAdmin):
    list_display = ['nom', 'adresse', 'email', 'telephone']  # Corrected field name

admin.site.register(Fournisseur, AdminFournisseur)

admin.site.register(Product, AdminProduct)
admin.site.register(Commande, AdminCommande)
