from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('hadu', views.hadu, name='hadu'),
    path('contacts', views.contacts, name='contacts')
]