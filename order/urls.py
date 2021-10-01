from django import forms
from django.urls import path
from .views import *
app_name="order"
urlpatterns = [
    path("", orderlistV, name="orders"),
    path("bill", conforder, name="conf"),
]
