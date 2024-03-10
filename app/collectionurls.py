from django.urls import path
from . import collectionviews

urlpatterns = [
    path("collections", view=collectionviews.get_collections, name="all collections"),
    path("coll/<int:id>", view=collectionviews.get_collection, name="get collection"),
    path("createl", view=collectionviews.create_collection, name="create collection"),
    path("addsongs", view=collectionviews.add_songs, name="add songs"),
]