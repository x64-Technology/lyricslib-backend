from rest_framework.response import Response
from .serializer import SongLyricsSerializer, SearchSongLyricsSerializer, SongForHome, SongCollectionSerializerPart
from .models import SongLyric, SongCollection
from rest_framework.decorators import api_view
from rest_framework import status
from django.db.models import Q 

@api_view()
def home_view(request):
    context = {}
    latest_songs = SongLyric.objects.order_by("publish")[:10]
    coll = SongCollection.objects.all()[:4]

    context["latest_songs"] = SongForHome(latest_songs, many=True).data
    context["collections"] = SongCollectionSerializerPart(coll, many=True).data

    return Response(data=context)

@api_view(["POST"])
def create_song(request):
    seri = SongLyricsSerializer(data=request.data)
    if seri.is_valid():
        seri.save()
        return Response(data={"message":"song lyrics created"}, status=status.HTTP_201_CREATED)
    else : return Response(data={"message":"failed to created song"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(["GET"])
def get_all_song(request):
    query = SongLyric.objects.all()
    print(query)
    ser = SongLyricsSerializer(query, many=True)
    return Response(data=ser.data, status=status.HTTP_200_OK)

@api_view(["GET"])
def get_song(request, id:int):
    try:
        query = SongLyric.objects.get(id=id)
        ser = SongLyricsSerializer(query)
        return Response(data=ser.data, status=status.HTTP_200_OK)
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
            Q(writer__icontains=search_query))

        ser = SearchSongLyricsSerializer(query, many=True)
        return Response(data=ser.data, status=status.HTTP_200_OK)
    return Response(data={"message":"empty song query"}, status=status.HTTP_400_BAD_REQUEST)

