from django.contrib import admin
from django.urls import path, include
from .views import *

app_name = 'home'

urlpatterns = [
    path('', servicesV, name="home"),
    path('sercvices/', allservices, name="serv"),
    path('rooms/', allrooms, name="room"),
    path('revs/', allerv, name="rev"),
    path('room/<slug:slug>', roomdetailsV, name="romdet"),
    path('services/<int:id>', servicesdetails, name="servdet"),
]
