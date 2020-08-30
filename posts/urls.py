from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("group/<slug>/", views.group_post, name = "groups")
<<<<<<< HEAD
]
=======
]
>>>>>>> caeee0f63cd0b9995b908f48cbcac21254cc1347
