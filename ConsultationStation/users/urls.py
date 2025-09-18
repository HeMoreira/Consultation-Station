from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('login/', views.loginView, name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='success'), name='logout'),
    path('registration/', views.registrationView, name='registration'),
]