from rest_framework.response import Response
from .serializer import SongLyricsSerializer, SearchSongLyricsSerializer
from .models import SongLyrics
from rest_framework.decorators import api_view
from rest_framework import status
from django.db.models import Q 

@api_view(["POST"])
def create_song(request):
    seri = SongLyricsSerializer(data=request.data)
    if seri.is_valid():
        seri.save()
        return Response(data={"message":"song lyrics created"}, status=status.HTTP_201_CREATED)
    else : return Response(data={"message":"failed to created song"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(["GET"])
def get_all_song(request):
    query = SongLyrics.objects.all()
    ser = SongLyricsSerializer(query, many=True)
    return Response(data=ser.data, status=status.HTTP_200_OK)

@api_view(["GET"])
def get_song(request, id:int):
    try:
        query = SongLyrics.objects.get(id=id)
        ser = SongLyricsSerializer(query)
        return Response(data=ser.data, status=status.HTTP_200_OK)
    except Exception as e:
        return Response(data={"message":"song not found"}, status=status.HTTP_404_NOT_FOUND)

@api_view(["GET"])
def search_song(request):
    search_query = request.GET.get('query')
    if search_query :
        query = SongLyrics.objects.filter(
            Q(name__icontains=search_query) |
            Q(album__icontains=search_query) |
            Q(singer__icontains=search_query) |
            Q(writer__icontains=search_query))

        ser = SearchSongLyricsSerializer(query, many=True)
        return Response(data=ser.data, status=status.HTTP_200_OK)
    return Response(data={"message":"empty song query"}, status=status.HTTP_400_BAD_REQUEST)

