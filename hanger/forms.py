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

    def __init__(self, *args, **kwargs):
            user = kwargs.pop('user', None)
            super().__init__(*args, **kwargs)
            
            if user:
                self.fields['items'].queryset = Item.objects.filter(user=user)
