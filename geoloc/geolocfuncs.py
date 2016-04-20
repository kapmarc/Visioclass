# -*- coding: utf-8 -*-
'''
Created on 7 janv. 2016

@author: kaplan
'''

from Visioclass.models import LocGeo

def getLocByName(name,user):
    userlocs = LocGeo.objects.get(user = user, name=name)
    #if len(userlocs)>0:
    #    return userlocs[0]
    #else:
    #    return None
    return userlocs
    
def getUserLocs(user):
    return LocGeo.objects.filter(user = user)

def getChildrens(loc):
    return LocGeo.objects.filter(ancestor = loc)

def getUserLocsByDepth(user, d):
    return LocGeo.objects.filter(user = user, depth = d)

def getCompleteUserLocs(user):
    completeLocs = LocGeo.objects.filter(user=user, depth = 3)
    return completeLocs

def colorTrans(colorName):
    colors = {'Gr':'gray',
              'Bg':'beige',
              'Lm':'lime',
              'Br':'brown',
              'Gn':'green',
              'Cy':'cyan',
              'Bl':'blue',
              'Yw':'yellow',
              'Or':'orange',
              'Rd':'red',
              'Rs':'pink',
              'Vt':'Violet'}
    return colors[colorName]

def nextColor(colorName, i=1):
    colors = ['gray','beige','lime','brown','green','cyan','blue','yellow','orange','red','pink','Violet']
    newcolorname='gray'
    try:
        newcolorname=colors[colors.index(colorName)+i %12]
    except:
        print('illegal color')
    return(newcolorname)