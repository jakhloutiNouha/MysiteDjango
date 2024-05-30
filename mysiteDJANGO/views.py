from django.shortcuts import render
from django.template import loader

def index(request):
    return render(request,'acceuil.html' )
from django.contrib import messages
from django.contrib.auth.decorators import login_required

