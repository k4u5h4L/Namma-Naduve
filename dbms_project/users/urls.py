from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('', views.landing_page, name='landing_page'),
    path('login/', views.login, name='login_page'),
    path('logout/', views.logout, name='logout_page'),
    path('register/', views.register, name='register_page'),
]
