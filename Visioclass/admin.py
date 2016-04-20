# -*- coding: utf-8 -*-
'''
Created on 2 janv. 2016

@author: kaplan
'''
from django.contrib import admin
from Visioclass.models import LocGeo, Profile, Etiquette

admin.site.register(LocGeo)
admin.site.register(Profile)
admin.site.register(Etiquette)