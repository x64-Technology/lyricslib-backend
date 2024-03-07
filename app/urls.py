from django.urls import path
from . import songviews, collectionviews

urlpatterns = [
    ## home
    path("", view=songviews.home_view, name="home"),

    ## songs
    path("allsong", view=songviews.get_all_song, name="getall"),
    path("create", view=songviews.create_song, name="create"),
    path("get/<int:id>", view=songviews.get_song, name="get"),
    path("search", view=songviews.search_song, name="search"),

    ## collections
    path("allcoll", view=collectionviews.get_collections, name="all collections"),
    path("coll/<int:id>", view=collectionviews.get_collection, name="get collection"),
    path("create", view=collectionviews.create_collection, name="create collection"),
    path("addsongs", view=collectionviews.add_songs, name="add songs"),
]