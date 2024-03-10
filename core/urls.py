from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/home/", include("api.urls")),
    path("api/song/", include("api.songurls")),
    path("api/collection/", include("api.collectionurls")),
]
