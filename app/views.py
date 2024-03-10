from rest_framework.response import Response
from .serializer import SearchSongLyricsSerializer, SongForHome, SongCollectionSerializerPart
from .models import SongLyric, SongCollection
from rest_framework.decorators import api_view
from rest_framework import status
from django.db.models import Q


@api_view(["GET"])
def home_view(request):
    context = {}
    latest_songs = SongLyric.objects.order_by("publish")[:10]
    coll = SongCollection.objects.all()[:5]

    context["latest_songs"] = SongForHome(latest_songs, many=True).data
    context["collections"] = SongCollectionSerializerPart(coll, many=True).data

    return Response(data=context)


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