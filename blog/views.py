# Dans le fichier views.py de votre application "blog"
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Post

class ListePostes(ListView):
    model = Post
    template_name = 'blog/liste_postes.html'

class DetailPoste(DetailView):
    model = Post
    template_name = 'blog/detail_poste.html'

class CreerPoste(CreateView):
    model = Post
    template_name = 'blog/creer_poste.html'
    fields = ['title', 'content', 'status', 'image']
    success_url = reverse_lazy('liste_postes')

class ModifierPoste(UpdateView):
    model = Post
    template_name = 'blog/modifier_poste.html'
    fields = ['title', 'content', 'status', 'image']
    success_url = reverse_lazy('liste_postes')

class SupprimerPoste(DeleteView):
    model = Post
    template_name = 'blog/supprimer_poste.html'
    success_url = reverse_lazy('liste_postes')
