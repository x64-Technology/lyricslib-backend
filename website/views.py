from django.shortcuts import render
from api.models import SongLyric, SongCollection
# Create your views here.

def index(request):
    songs = SongLyric.objects.all()[:23]
    colls = SongCollection.objects.all()[:12]
    return render(request=request, template_name="index.html", context={"songs":songs, "collections":colls})

def songs(request):
    print("getting")
    songs = SongLyric.objects.all()#.values("id", "name", "image", "slug")
    return render(request=request, template_name="songs.html", context={"songs":songs})