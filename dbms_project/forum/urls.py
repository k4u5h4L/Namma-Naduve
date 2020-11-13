from django.urls import path
from .views import postview

from . import views

urlpatterns = [
    path('', views.home_page, name='home_page'),
    # path('create/', postcreate.as_view(), name='postcreate'),
    path('search/<str:query>/', views.search_results, name='search_results'),
    path('post/<int:pk>/', postview.as_view(),name='post_page'),
    path('user/about/<str:usr_name>/',
         views.profile_about_page, name='profile_about_page'),
    path('user/<str:usr_name>/', views.profile_page, name='profile_page'),
    path('faq/', views.faq_page, name='faq_page'),
]
