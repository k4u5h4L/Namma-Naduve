from django.urls import path

from . import views

urlpatterns = [
    path('', views.homePage, name='homePage'),
    path('search=<str:query>/', views.searchResults, name='searchResults'),
    path('faq/', views.faqPage, name='faqPage'),
]
