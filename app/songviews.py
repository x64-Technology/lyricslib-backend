from rest_framework.response import Response
from .serializer import SongLyricsSerializer, SearchSongLyricsSerializer, SongForHome, SongCollectionSerializerPart
from .models import SongLyric, SongCollection
from rest_framework.decorators import api_view
from rest_framework import status
from django.db.models import Q 
from datetime import datetime

@api_view(["GET"])
def home_view(request):
    context = {}
    latest_songs = SongLyric.objects.order_by("publish")[:10]
    coll = SongCollection.objects.all()[:4]

    context["latest_songs"] = SongForHome(latest_songs, many=True).data
    context["collections"] = SongCollectionSerializerPart(coll, many=True).data

    return Response(data=context)

@api_view(["POST"])
def create_song(request):
    request.data["title"] = request.data["name"] + " lyrics"
    request.data["slug"] = request.data["title"].replace(" ", "-")
    request.data["publish"] = datetime.strptime(request.data["publish"], "%d/%m/%Y").date()
    seri = SongLyricsSerializer(data=request.data)
    try:
        if seri.is_valid(raise_exception=True):
            seri.save()
            return Response(data={"message":"song lyrics created"})
    except Exception as e:
        return Response(data={"message":str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(["GET"])
def get_all_song(request):
    query = SongLyric.objects.all()
    print(query)
    ser = SongForHome(query, many=True)
    return Response(data=ser.data)

@api_view(["GET"])
def get_song(request, id:int):
    try:
        query = SongLyric.objects.get(id=id)
        ser = SongLyricsSerializer(query)
        return Response(data=ser.data)
    except Exception as e:
        return Response(data={"message":"song not found"}, status=status.HTTP_404_NOT_FOUND)

@api_view(["GET"])
def get_song_by_slug(request, slug:str):
    try:
        query = SongLyric.objects.get(slug__icontains=slug)
        ser = SongLyricsSerializer(query)
        return Response(data=ser.data)
    except Exception as e:
        return Response(data={"message":"song not found"}, status=status.HTTP_404_NOT_FOUND)

@api_view(["GET"])
def search_song(request):
    search_query = request.GET.get('query')
    if search_query :
        query = SongLyric.objects.filter(
            Q(name__icontains=search_query) |
            Q(album__icontains=search_query) |
            Q(singer__icontains=search_query) |
            Q(writer__icontains=search_query) |
            Q(music__icontains=search_query) |
            Q(title__icontains=search_query) |
            Q(slug__icontains=search_query))

        ser = SearchSongLyricsSerializer(query, many=True)
        return Response(data=ser.data)
    return Response(data={"message":"empty song query"}, status=status.HTTP_400_BAD_REQUEST)

