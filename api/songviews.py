from rest_framework.response import Response
from .serializer import SongLyricsSerializer, SongForHome
from .models import SongLyric
from rest_framework.decorators import api_view
from rest_framework import status
from datetime import datetime

@api_view(["POST"])
def create_song(request):
    #request.data["title"] = request.data["name"] + " lyrics"
    #request.data["slug"] = request.data["title"].replace(" ", "-")
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
        query = SongLyric.objects.filter(slug__icontains=slug)[0]
        ser = SongLyricsSerializer(query)
        return Response(data=ser.data)
    except Exception as e:
        return Response(data={"message":"song not found"}, status=status.HTTP_404_NOT_FOUND)
    