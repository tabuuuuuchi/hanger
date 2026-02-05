from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index_view, name='index'),
    path('item/', views.ListItemView.as_view(), name='list-item'),
    path('item/<int:pk>/detail/', views.DetailItemView.as_view(), name='detail-item'),
    path('item/create/', views.CreateItemView.as_view(), name='create-item'),
    path('item/<int:pk>/update/', views.UpdateItemView.as_view(), name='update-item'),
    path('item/<int:pk>/delete/', views.DeleteItemView.as_view(), name='delete-item'),
    path('outfit/', views.ListOutfitView.as_view(), name='list-outfit'),
    path('outfit/<int:pk>/detail/', views.DetailOutfitView.as_view(), name='detail-outfit'),
    path('outfit/<int:outfit_id>/<int:pk>/detail/', views.DetailOutfitItemView.as_view(), name='detail-outfit-item'),
    path('outfit/<int:outfit_id>/<int:pk>/update/', views.UpdateOutfitItemView.as_view(), name='update-outfit-item'),
    path('outfit/<int:outfit_id>/<int:pk>/delete/', views.DeleteOutfitItemView.as_view(), name='delete-outfit-item'),
    path('outfit/create/', views.CreateOutfitView.as_view(), name='create-outfit'),
]