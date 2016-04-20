# -*- coding: utf-8 -*-
'''
Created on 26 déc. 2015

@author: kaplan
'''
from django.http import HttpResponse 
from django.shortcuts import render_to_response, redirect, render
from registration.forms import RegistrationForm 
from django.contrib.auth import login, authenticate, logout
from Visioclass.forms import LoginForm, LocForm
from Visioclass.models import LocGeo
import Visioclass
from django.http.response import HttpResponseRedirect



def welcome(request):
    user = request.user
    form = LoginForm()
    return(render(request, 'base.html', locals()))

def error(request):
    return(render_to_response("errors/notfound.html", locals()))


def connexion(request):
    error = False
    disable_right_navbar = True
    
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["login"]  # Nous récupérons le nom d'utilisateur
            password = form.cleaned_data["passw"]  # … et le mot de passe
            user = authenticate(username=username, password=password)  #Nous vérifions si les données sont correctes
            if user:  # Si l'objet renvoyé n'est pas None
                login(request, user)  # nous connectons l'utilisateur
            else: #sinon une erreur sera affichée
                error = True
    else:
        form = RegistrationForm()

    return render(request, 'connexion.html',locals())

def deconnexion(request):  
    logout(request)                                                                                     
    return redirect('accueil')

def voir(request):
    return(render(request, 'tags/voir.html' ,locals()))

def creer(request):
    return(render(request, 'tags/creer.html', locals()))

def submitnewloc(request):
    return(redirect('accueil'))