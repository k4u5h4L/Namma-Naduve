from django.urls import path


from . import views

urlpatterns = [
     path('search/', views.search_results, name='search_results'),
     path('post/<int:post_id>/', views.post_page, name='post_page'),
     path('create/post/', views.create_post, name='create_post_page'),
     path('create/reply/<int:post_id>',
         views.create_reply, name='create_reply_page'),
     path('user/<str:usr_name>/about/',
         views.profile_about_page, name='profile_about_page'),
     path('user/<str:usr_name>/update/pic/',
         views.profile_picture_page, name='profile_pic_update_page'),
     path('user/<str:usr_name>/update/',
         views.profile_update_page, name='profile_update_page'),
     path('user/<str:usr_name>/', views.profile_page, name='profile_page'),
     path('delete/<int:post_id>',views.delete_post,name='delete'),
     path('faq/', views.faq_page, name='faq_page'),
     path('', views.home_page, name='home_page'),
]
