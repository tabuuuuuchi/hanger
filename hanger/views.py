from django.shortcuts import render, get_object_or_404
from django.urls import reverse ,reverse_lazy
from django.http import HttpResponseRedirect
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from .models import Item, Season, Outfit
from .forms import OutfitForm




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


class DeleteItemView(DeleteView):       #アイテム詳細
    template_name = 'hanger/item_delete.html'
    model = Item
    success_url = reverse_lazy('list-item')


class UpdateItemView(UpdateView):
    template_name = 'hanger/item_update.html'
    model = Item
    fields = ('name', 'brand', 'category', 'thumbnail')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse('detail-item', kwargs={'pk': self.object.id})
    

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


class DetailOutfitItemView(DetailView):       #コーデ→アイテム詳細
    template_name = 'hanger/item_detail.html'
    model = Item

    def get_object(self, queryset=None):
        outfit_id = self.kwargs.get('outfit_id')
        item_id = self.kwargs.get('pk')

        return get_object_or_404(Item, pk=item_id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['outfit'] = get_object_or_404(Outfit, pk=self.kwargs.get('outfit_id'))

        return context
    

class UpdateOutfitItemView(UpdateView):       #コーデ→アイテム編集
    template_name = 'hanger/item_update.html'
    model = Item
    fields = ('name', 'brand', 'category', 'thumbnail')

    def get_object(self, queryset=None):
        outfit_id = self.kwargs.get('outfit_id')
        item_id = self.kwargs.get('pk')

        return get_object_or_404(Item, pk=item_id)
    
    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        context['outfit'] = get_object_or_404(Outfit, pk=self.kwargs.get('outfit_id'))

        return context

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse('detail-outfit-item', kwargs={'outfit_id': self.kwargs.get('outfit_id'), 'pk': self.object.id})

    

class DeleteOutfitItemView(DeleteView):       #コーデ→アイテム削除
    template_name = 'hanger/item_delete.html'
    model = Item
    def get_success_url(self):
        success_url = reverse('detail-outfit', kwargs={'pk': self.kwargs.get('outfit_id')})
        return success_url
    
    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        context['outfit'] = get_object_or_404(Outfit, pk=self.kwargs.get('outfit_id'))

        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        outfit_id = self.kwargs.get('outfit_id')
        outfit_object = Outfit.objects.get(id=outfit_id)
        outfit_object.items.remove(self.object.id)
            
        return HttpResponseRedirect(self.get_success_url())
    

class CreateOutfitView(CreateView):    #コーデ登録
    template_name = 'hanger/outfit_create.html'
    model = Item
    form_class = OutfitForm
    success_url = reverse_lazy('list-outfit')

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["item"] = Item.objects.all()
        return ctx
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
