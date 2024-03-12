from django.shortcuts import render
from api.models import SongLyric, SongCollection
# Create your views here.

def index(request):
    songs = SongLyric.objects.all().values("name", "album", "singer", "image", "slug")[:20]
    colls = SongCollection.objects.all()[:12]
    return render(request=request, template_name="index.html", context={"songs":songs, "collections":colls})

def songs(request): ## TODO impliment paginations
    songs = SongLyric.objects.all().values("id", "name", "image", "slug")
    return render(request=request, template_name="songs.html", context={"songs":songs})

def get_lyric(request, slug):
    try:
        lyrics = SongLyric.objects.get(slug=slug)
        album_songs = SongLyric.objects.filter(album__icontains=lyrics.album).exclude(id=lyrics.id).values("name", "singer", "slug")
        singer_songs = SongLyric.objects.filter(singer__icontains=lyrics.singer).exclude(id=lyrics.id).values("name", "album", "slug")[:10]

        return render(request=request, template_name="lyrics.html", context={"lyrics":lyrics, "album_songs":album_songs, "singer_songs":singer_songs})
    except Exception as e:
        print(e)
        return render(request=request, template_name="notfound.html")
    
def album_songs(request, album_name):
    try:
        album_songs = SongLyric.objects.filter(album=album_name).values("name", "image")
        return render(request=request, template_name="album_songs.html", context={"album":album_name, "songs":album_songs})
    except Exception as e:
        print(e)
        return render(request=request, template_name="notfound.html")