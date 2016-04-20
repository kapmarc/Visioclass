# -*- coding: utf-8 -*-
'''
Created on 4 janv. 2016

@author: kaplan
'''
from django.conf.urls import url

urlpatterns = [
    url(r'^$','geoloc.views.locgeo', name='locgeo'),
    url(r'^([\w ]*)/$', 'geoloc.views.locgeo'),
    url(r'^([\w ]*)/([\w ]*)/$', 'geoloc.views.locgeo'),
    url(r'^([\w ]*)/([\w ]*)/([\w ]*)/$', 'geoloc.views.locgeo'),
    url(r'^delete', 'geoloc.views.delete', name = 'delete'),
    url(r'^create', 'geoloc.views.create', name = 'create'),
    url(r'^update', 'geoloc.views.update', name = 'update'),
    url(r'summary', 'geoloc.views.summary', name = 'summary')
]
