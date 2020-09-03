from django.urls import path
from posts import views

urlpatterns = [
    path("", views.index, name="index"),
    path("group/<slug>/", views.group_posts, name = "groups")

]

