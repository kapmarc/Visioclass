# -*- coding: utf-8
"""Visioclass URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from Visioclass import views
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^$', views.welcome),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accueil/', views.welcome, name='accueil'),
    url(r'^error/', 'Visioclass.views.error', name='error'),
    #url(r'^accueilconnected/', views.welcome_con),
    #url(r'^register/', views.register, name ='register'),
    #url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^accounts/', include('registration.backends.simple.urls')),
    url(r'^connexion/$', 'Visioclass.views.connexion', name='connexion'),
    url(r'^deconnexion/$', 'Visioclass.views.deconnexion', name='deconnexion'),
    url(r'^tags/listview/', 'Visioclass.views.voir'),
    url(r'^tags/create/', 'Visioclass.views.creer'),
    #url pour les créations de localisations géographiques
    url(r'^geoloc/', include('geoloc.urls')),
    #url(r'^tags/geoloc/$','Visioclass.views.locgeo'),
    #url(r'^tags/geoloc/(\w*)/$', 'Visioclass.views.locgeo'),
    #url(r'^tags/geoloc/(\w*)/(\w*)/$', 'Visioclass.views.locgeo'),
    #url(r'^tags/geoloc/(\w*)/(\w*)/(\w*)/$', 'Visioclass.views.locgeo'),
]
