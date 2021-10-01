from django import forms
from django.urls import path
from .views import *
app_name="user"
urlpatterns = [
    path("<int:id>", userv, name="userf"),
    path("cancel-book", DeletRoom, name="cancelbook"),
    path("delete-all", deletallroom, name="delall"),
]
