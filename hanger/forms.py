from django import forms
from .models import Item, Outfit, Season

class OutfitForm(forms.ModelForm):    #コーデ登録フォーム
    class Meta:
        model = Outfit
        fields = ['name', 'thumbnail', 'seasons', 'items']
        widgets = {
            'seasons': forms.CheckboxSelectMultiple(),
            'items': forms.CheckboxSelectMultiple(),
        }