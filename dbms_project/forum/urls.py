from django.urls import path

from . import views

urlpatterns = [
    path('search/', views.search_results, name='search_results'),
    path('post/<int:post_id>/', views.post_page, name='post_page'),
    path('create/post/', views.create_post, name='create_post_page'),
    path('user/about/<str:usr_name>/',
         views.profile_about_page, name='profile_about_page'),
    path('user/<str:usr_name>/', views.profile_page, name='profile_page'),
    path('faq/', views.faq_page, name='faq_page'),
    path('', views.home_page, name='home_page'),
]
