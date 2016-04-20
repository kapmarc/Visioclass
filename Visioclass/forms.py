# -*- coding: utf-8 -*-
'''
Created on 27 déc. 2015

@author: kaplan
'''
from django import forms

class LoginForm(forms.Form):
    login = forms.CharField(label = 'Login', max_length=30)
    passw = forms.CharField(label = 'Mot de passe', widget = forms.PasswordInput)
    
class LocForm(forms.Form):
    COLORS = (('Gr','gray'),
              ('Bg','beige'),
              ('Lm','lime'),
              ('Br','brown'),
              ('Gn','green'),
              ('Cy','cyan'),
              ('Bl','blue'),
              ('Yw','yellow'),
              ('Or','orange'),
              ('Rd','red'),
              ('Rs','pink'),
              ('Vt','Violet')
              )
    nom = forms.CharField(max_length=20)
    description = forms.CharField(widget=forms.Textarea, max_length=300)
    couleur = forms.ChoiceField(choices=COLORS)
