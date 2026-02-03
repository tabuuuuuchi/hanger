from django.db import models


CATEGORY = (('トップス', 'トップス'), ('パンツ', 'パンツ'), ('アウター', 'アウター'), ('シューズ', 'シューズ'), ('アクセサリー', 'アクセサリー'), ('その他', 'その他'))
SEASON = (('spring', 'spring'), ('summer', 'summer'), ('autumn', 'autumn'), ('winter', 'winter'))


class Item(models.Model):   #アイテム
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=100, null=True)
    thumbnail = models.ImageField(null=True, blank=True)
    category = models.CharField(
        max_length=100,
        choices = CATEGORY
    )
    
    def __str__(self):
        return self.name
    

class Season(models.Model):    #季節
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Outfit(models.Model):  #コーデ
    name = models.CharField(max_length=100)
    thumbnail = models.ImageField(null=True, blank=True)
    seasons = models.ManyToManyField(Season)
    items = models.ManyToManyField(Item)

    def __str__(self):
        return self.name

