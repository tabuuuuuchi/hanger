from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Item, Season, Outfit



class ListItemView(ListView):          #アイテム一覧
    template_name = 'hanger/item_list.html'
    model = Item


class DetailItemView(DetailView):       #アイテム詳細
    template_name = 'hanger/item_detail.html'
    model = Item


class CreateItemView(CreateView):
    template_name = 'hanger/item_create.html'
    model = Item


class ListOutfitView(ListView):     #コーデ一覧
    template_name = 'hanger/outfit_list.html'
    model = Outfit

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["season"] = Season.objects.all()
        return ctx

class DetailOutfitView(DetailView):    #コーデ詳細
    templates_name = 'hanger/outfit_detail.html'
    model = Outfit


def index_view(request):    #ログイン/会員登録画面

    return render(request, 'hanger/index.html')


