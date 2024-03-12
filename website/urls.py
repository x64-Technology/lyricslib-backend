from django.urls import path
from . import views

urlpatterns = [
    path("", view=views.index),
    path("sng", view=views.songs),
    path("lyric/<slug:slug>", view=views.get_lyric),
    path("album/<str:album_name>", view=views.album_songs)
]