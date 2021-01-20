from django.urls import path
from posts import views

urlpatterns = [
    path('', views.index),
    path("group/<slug:slug>", views.group_posts),
]