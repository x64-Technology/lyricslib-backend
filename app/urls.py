from django.urls import path
from . import songviews, collectionviews

urlpatterns = [
    ## songs
    path("allsong", view=songviews.get_all_song, name="getall"),
    path("create", view=songviews.create_song, name="create"),
    path("get/<int:id>", view=songviews.get_song, name="get"),
    path("search", view=songviews.search_song, name="search"),

    ## collections
    path("allcoll", view=collectionviews.get_collections, name="all collections"),
    path("create", view=collectionviews.create_collection, name="create collection"),
    path("addsongs", view=collectionviews.add_songs, name="add songs"),
]