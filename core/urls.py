from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("home/", include("app.urls")),
    path("song/", include("app.songurls")),
    path("collection/", include("app.collectionurls")),
]
