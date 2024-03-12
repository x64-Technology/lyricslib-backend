from django.urls import path
from . import views

urlpatterns = [
    path("", view=views.index),
    path("sng", view=views.songs),
    path("lyric/<slug:slug>", view=views.get_lyric),
    path("album/<str:album_name>", view=views.album_songs),
    path("colls", view=views.get_collections),
    path("coll/<int:collId>", view=views.collection_songs),
    
    path("search", view=views.search),
]