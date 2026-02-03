from django.shortcuts import render
from django.urls import reverse_lazy
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
    fields = ('name', 'brand', 'category', 'thumbnail')
    success_url = reverse_lazy('list-item')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


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


