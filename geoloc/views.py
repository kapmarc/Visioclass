# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response, redirect, render 
from django.contrib.auth.decorators import login_required
from Visioclass.forms import LocForm
from Visioclass.models import LocGeo
import Visioclass
from django.http.response import HttpResponseRedirect
from geoloc.geolocfuncs import *
from django.utils.http import urlquote

# Create your views here.

@login_required()
def locgeo(request, loc1='null', loc2='null', loc3='null'):
    user = request.user
    userlocs = getUserLocs(user)
    userlocnames = map(lambda x:urlquote(x.name),userlocs)
            
    form = LocForm(auto_id="id_%s_create")
    editForm = LocForm(auto_id="id_%s_edit")
    creation_authorized = True
    currentloc = 'null'
    
    if (loc1!='null' and not(urlquote(loc1) in userlocnames)) or (loc2!='null' and not(urlquote(loc2) in userlocnames)) or (loc3!='null' and not(urlquote(loc3) in userlocnames)):
        return(redirect('error'))
    if (loc1!='null' and getLocByName(loc1, user).depth != 1) or (loc2!='null' and getLocByName(loc2, user).depth != 2) or (loc3!='null' and getLocByName(loc3, user).depth != 3):
        return(redirect('error'))
        
        
    
    if loc1 == 'null':
        root = True
        sublocs = list(filter(lambda x:x.ancestor==None,userlocs))
    elif loc2 == 'null':
        currentloc = list(filter(lambda x:x.name==loc1, userlocs))[0]
        sublocs = list(filter(lambda x:x.ancestor==currentloc,userlocs))
    elif loc3 == 'null':
        currentloc = list(filter(lambda x:x.name==loc2, userlocs))[0]
        sublocs = list(filter(lambda x:x.ancestor==currentloc,userlocs))
    else:
        currentloc = list(filter(lambda x:x.name==loc3, userlocs))[0]
        creation_authorized= False
    if currentloc != 'null':
        description = currentloc.description
        
    urlpref =''
    colors= ['white', 'white', 'white']
    
    if currentloc != 'null':
        gen = currentloc.getGenealogy()
    else:
        gen = []
    i=0
    for loc in gen:
        if loc != None:
            urlpref = urlpref +loc.name+'/'
            colors[i]=colorTrans(loc.color)
        i+=1
    if currentloc=='null':
        currentcol='white'
    else:
        currentcol = colorTrans(currentloc.color)
    
    
    return(render(request, 'geoloc/locs.html', locals()))

@login_required()
def create(request):
    user = request.user
    userlocs = getUserLocs(user)
    userlocnames = map(lambda x:urlquote(x.name),userlocs)
    
    # S'il y a une requête POST, on l'enregistre
    if len(request.POST) >0:
        form = LocForm(request.POST)
        if request.POST['nom'] in userlocnames:
            return(HttpResponseRedirect('error'))
        elif form.is_valid():
            fathername = request.POST['father-name']
            if fathername != '':
                ancestor = list(filter(lambda x:x.name==fathername,userlocs))[0]
            else:
                ancestor = None
            o = Visioclass.models.LocGeo()
            o.user = user
            o.name = request.POST['nom']
            o.description = request.POST['description']
            o.ancestor = ancestor
            o.color = request.POST['couleur']
            if ancestor != None:
                o.depth=ancestor.depth+1
            else:
                o.depth=1
            o.save()
        request.POST=None
        #redirection sans requête POST
        #recalculer la bonne adresse
        url = '/'
        gen = o.getGenealogy()
        for loc in gen:
            if loc != None:
                url = url +loc.name+'/'
        #Le calcul de l'url ne marche pas. Pourquoi?
    return(redirect('locgeo'))

@login_required()
def delete(request):
    if len(request.POST) >0:
        locname = request.POST['loc-name']
        user = request.user
        o = getLocByName(locname, user)
        o.delete()
    return(redirect('locgeo'))

@login_required()
def update(request):
    if len(request.POST) >0:
        locname = request.POST['loc-name']
        user = request.user
        o = getLocByName(locname, user)
        o.name = request.POST['nom']
        o.description = request.POST['description']
        o.color = request.POST['couleur']
        o.save()
    return(redirect('locgeo'))

@login_required()
def summary(request):
    user = request.user
    userlocs1 = getUserLocsByDepth(user,1)
    userlocs2 = getUserLocsByDepth(user,2)
    userlocs3 = getUserLocsByDepth(user,3)
    return(render(request, 'geoloc/summary.html', locals()))