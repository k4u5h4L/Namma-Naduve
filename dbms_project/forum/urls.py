from django.urls import path

from . import views

urlpatterns = [
    path('', views.homePage, name='homePage'),
    path('search=<str:query>/', views.searchResults, name='searchResults'),
    path('<str:usr_name>/', views.profilePage, name='profilePage'),
    path('faq/', views.faqPage, name='faqPage'),
]
