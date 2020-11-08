from django.urls import path
from posts import views

urlpatterns = [
    path('', views.index), 
    path('user', views.account),
    path('user/1', views.user_first),
    path('user/<int:user-id>', views.user_page),
    path('user/2', views.user_second),
    path('user/login', views.login),
    path('user/logout', views.logout),
]