from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import SignupView
from . import views

app_name = 'accounts'

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('signup/', SignupView.as_view(), name='signup'),
]