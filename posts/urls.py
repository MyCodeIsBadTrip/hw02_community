from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("group/<slug>/", views.group_post, name = "groups")
<<<<<<< HEAD
]

