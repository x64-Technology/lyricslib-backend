from django.shortcuts import render, redirect
from api.models import SongLyric, SongCollection
from django.db.models import Q

def index(request):
    songs = SongLyric.objects.all().values("name", "album", "singer", "image", "slug")[:14]
    colls = SongCollection.objects.all()[:6]
    albums = SongLyric.objects.all().values("album").distinct()[:15]
    return render(request=request, template_name="index.html", context={"songs":songs, "collections":colls, "albums":albums})

def songs(request): ## TODO impliment paginations
    songs = SongLyric.objects.all().values("id", "name", "image", "slug")
    return render(request=request, template_name="songs.html", context={"songs":songs})

def get_lyric(request, slug):
    try:
        lyrics = SongLyric.objects.get(slug=slug)
        album_songs = SongLyric.objects.filter(album__icontains=lyrics.album).exclude(id=lyrics.id).values("name", "singer", "slug")
        singer_songs = SongLyric.objects.filter(singer__icontains=lyrics.singer).exclude(id=lyrics.id).values("name", "album", "slug")[:6]

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
    

def get_collections(request):
    collections = SongCollection.objects.all()[:14]
    return render(request=request, template_name="collections.html", context={"collections":collections})

def collection_songs(request, collId):
    try:
        songs = SongLyric.objects.filter(songcollection__id=collId).values("name", "image", "slug")
        return render(request=request, template_name="collection_songs.html", context={"songs":songs})
    except Exception as e:
        print(e)
        return render(request=request, template_name="notfound.html")
    

## TODO impliment paginations
def search(request):
    query = request.GET.get('query')

    if query :
        result = SongLyric.objects.filter(
            Q(name__icontains=query) |
            Q(album__icontains=query) |
            Q(singer__icontains=query) |
            Q(writer__icontains=query) |
            Q(music__icontains=query) |
            Q(title__icontains=query) |
            Q(slug__icontains=query)).values("name", "album", "slug", "image")[:20]
        
        return render(request=request, template_name="search.html", context={"result":result, "query":query})
    return render(request=request, template_name="search.html", context={"result":query})
