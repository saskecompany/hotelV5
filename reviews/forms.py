from django import forms
from django.forms import widgets
from .models import reM

class reF(forms.ModelForm):
    class Meta:
        model = reM
        fields = '__all__'
        widgets = {
            'reimage':forms.FileInput(),
            'rename': forms.TextInput(attrs={'id':'revf', 'placeholder':'enter your name'}),
            'redes': forms.TextInput(attrs={'id':'revf', 'placeholder':'enter your comment'}),
            'rerate': forms.NumberInput(attrs={'id':'revf', 'placeholder':'enter your rate'}),
        }
