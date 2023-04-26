from django.urls import path

from . import views

app_name = "app"

urlpatterns = [
    path("", views.index, name="index"),
    path("read-online/", views.read_online, name="read_online"),
    path("read/<str:id>/", views.read_book, name="read_book"),
]
