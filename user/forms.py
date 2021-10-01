from django import forms
from .models import *

class userf(forms.ModelForm):
    
    class Meta:
        model = user
        exclude=["usip", "usbookfav", "usrobook", "usname", "lname", "fname", "usphone", "nname", "usaddress"]