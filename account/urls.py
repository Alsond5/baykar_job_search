from . import views
from django.urls import path

urlpatterns = [
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('email-sender', views.forgot_pw, name='forgot_pw'),
    path('change-password', views.reset_pw, name='reset_pw'),
    path('confirm', views.confirm, name='confirmation'),
    path('profile', views.profile, name='profile'),
    path('delete-account(<int:id>', views.delete_account, name='delete_account'),
]

