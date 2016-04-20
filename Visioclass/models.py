# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields.related import ForeignKey

# Create your models here.
'''
Created on 28 déc. 2015

@author: kaplan
'''
class Profile(models.Model):
    user = models.OneToOneField(User)  # La liaison OneToOne vers le modèle User
    privilege = models.IntegerField()

    def __unicode__(self):
        return self.user.username
    def __str__(self):
        return self.user.username
    
class LocGeo(models.Model):
    """La classe de localisation géographique. Elle est structurée en arbre: chaque localisation peut avoir un ancetre""" 
    user = models.ForeignKey(User)
    name = models.CharField(max_length = 20)
    description = models.CharField(max_length = 300)
    ancestor = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    color = models.CharField(max_length=2)
    depth = models.IntegerField()
    
    class Meta:
        unique_together = (("user", "name"),)

    def __unicode__(self):
        return self.name
    
    def __str__(self):
        return self.name
    
    def getGenealogy(self):
        a = self
        t = []
        while a != None:
            t.append(a)
            a=a.ancestor
        #return t in reversed order
        return t[::-1]

class Etiquette(models.Model):
    """La classe qui décrit une étiquette. Une étiquette est décrit par:
        - l'utilisateur qui l'a créé
        - un triplet de couleurs
        - un triplet (position, lettre, chiffre)
        """
    user = models.ForeignKey(User)
    loc = models.ForeignKey('locGeo')
    tagPerso1 = models.CharField(max_length=2)
    tagPerso2 = models.CharField(max_length=2)
    identificateur1 = models.CharField(max_length=2)
    identificateur2 = models.CharField(max_length=2)
    identificateur3 = models.CharField(max_length=2)
    
    def __unicode__(self):
        return "{0},{1},{2}".format(self.identificateur1, self.identificateur2, self.identificateur3)
    def __str__(self):
        return "{0},{1},{2}".format(self.identificateur1, self.identificateur2, self.identificateur3)

    