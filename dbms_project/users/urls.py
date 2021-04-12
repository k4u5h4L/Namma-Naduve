from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('', views.landing_page, name='landing_page'),
    path('login/', views.login, name='login_page'),
    path('logout/', views.logout, name='logout_page'),
    path('register/', views.register, name='register_page'),
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name = "users/password_reset.html"), name="password_reeset"),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name="users/password_reset_done.html"), name="password_reset_done" ),
    path('password-reset/confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="users/password_reset_confirm.html"), name="password_reset_confirm" ),
    path('password-reset/complete/', auth_views.PasswordResetCompleteView.as_view(template_name="users/password_reset_complete.html"), name="password_reset_complete" )

    
]
