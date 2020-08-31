from django.urls import path

urlpatterns = [
    path("", views.index, name="index"),
    path("group/<slug>/", views.group_post, name = "groups")

]

