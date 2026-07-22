from django import forms
from .models import Item, Outfit
from django.core.exceptions import ValidationError

class ItemForm(forms.ModelForm):    #アイテム登録フォーム
    class Meta:
        model = Item
        fields = ['name', 'brand', 'category', 'thumbnail']

    def clean(self):
         cleaned_data = super().clean()
         thumbnail = cleaned_data.get('thumbnail')

         if not thumbnail:
              raise ValidationError({
                   'thumbnail': '画像ファイルが選択されていません。画像を洗濯してやり直してください。'
              })
         
         return cleaned_data
    


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

    def clean(self):
         cleaned_data = super().clean()
         thumbnail = cleaned_data.get('thumbnail')

         if not thumbnail:
              raise ValidationError({
                   'thumbnail': '画像ファイルが選択されていません。画像を洗濯してやり直してください。'
              })
         
         return cleaned_data
