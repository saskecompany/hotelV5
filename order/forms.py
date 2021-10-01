from django import forms
from .models import *

class orderF(forms.ModelForm):
    
    class Meta:
        model = order
        fields = "__all__"
