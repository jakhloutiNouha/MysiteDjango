from django.db import models
from django.db.models.fields.related import ForeignKey




class Category(models.Model):
    name = models.CharField(max_length=50)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name




class Fournisseur(models.Model):
    nom = models.CharField(max_length=100)
    adresse = models.TextField()  # Corrected field name 'adressse' to 'adresse'
    email = models.EmailField()
    telephone = models.CharField(max_length=20)  # Increased max_length for telephone number

    def __str__(self):
        return f"{self.nom} ({self.email})"

class Product(models.Model):
    TYPE_CHOICES = [
        ('fr', 'Frais'),
        ('cs', 'Conserver'),
        ('em', 'Emballé')
    ]

    title = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Changed to DecimalField for better precision
    description = models.TextField()
    fournisseur = models.ForeignKey(Fournisseur, on_delete=models.CASCADE, null=True)
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    image = models.ImageField(blank=True)
    date_added = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-date_added']

    def __str__(self):
        return self.title

class Commande(models.Model):
    items = models.TextField()  # Increased max_length for items
    total = models.DecimalField(max_digits=10, decimal_places=2)  # Changed to DecimalField for total amount
    nom = models.CharField(max_length=150)
    email = models.EmailField()
    address = models.CharField(max_length=200)
    ville = models.CharField(max_length=200)
    pays = models.CharField(max_length=200)  # Reduced max_length for country
    zipcode = models.CharField(max_length=20)  # Increased max_length for ZIP code
    date_commande = models.DateTimeField(auto_now=True)
    products = models.ManyToManyField(Product, through='CommandeItem', related_name='commandes')  # Many-to-Many relationship

    class Meta:
        ordering = ['-date_commande']

    def __str__(self):
        return self.nom

class CommandeItem(models.Model):
    commande = models.ForeignKey(Commande, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)  # Track quantity

    def __str__(self):
        return f"{self.quantity}x {self.product.title}"

class ProduitNC(Product):
    duree_garantie = models.CharField(max_length=100)  # Corrected field name 'Duree_garantie' to lowercase
