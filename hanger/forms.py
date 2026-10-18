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
                   'thumbnail': '画像ファイルが選択されていません。画像を選択してやり直してください。'
              })
         
         return cleaned_data
    


class OutfitForm(forms.ModelForm):    #コーデ登録フォーム
     class Meta:
        model = Outfit
        fields = ['name', 'thumbnail', 'seasons', 'items']
        widgets = {
            'seasons': forms.CheckboxSelectMultiple(),
            'items' : forms.CheckboxSelectMultiple(),
        }

     def __init__(self, *args, **kwargs):
            user = kwargs.pop('user', None)
            super().__init__(*args, **kwargs)
                      
            if user:

               field = self.fields["items"]
               field.queryset = Item.objects.filter(user=user)

               grouped_choices = {}

               for item in field.queryset:
                    category_label = item.category

                    grouped_choices.setdefault(category_label, []).append((
                         field.prepare_value(item),
                         field.label_from_instance(item),
                    ))

               field.choices = list(grouped_choices.items())

               bound_field = self["items"]

               self.item_groups = field.widget.get_context(
               name=bound_field.html_name,
               value=bound_field.value(),
               attrs={"id": bound_field.auto_id},
               )["widget"]["optgroups"]

     def clean(self):
         cleaned_data = super().clean()
         thumbnail = cleaned_data.get('thumbnail')

         if not thumbnail:
              raise ValidationError({
                   'thumbnail': '画像ファイルが選択されていません。画像を選択してやり直してください。'
              })
         
         return cleaned_data
