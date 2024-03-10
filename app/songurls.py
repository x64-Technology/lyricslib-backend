from django.urls import path
from . import songviews


urlpatterns = [
    path("songs", view=songviews.get_all_song, name="getall"),
    path("create", view=songviews.create_song, name="create"),
    path("get/<int:id>", view=songviews.get_song, name="get"),
    path("slug/<str:slug>", view=songviews.get_song_by_slug, name="get song by slug"),
]