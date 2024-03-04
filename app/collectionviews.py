from rest_framework.response import Response
from .serializer import SongCollectionSerializer
from .models import SongCollection, SongLyrics
from rest_framework.decorators import api_view
from rest_framework import status
from django.db.models import Q 

@api_view(["POST"])
def create_collection(request):
    ser = SongCollectionSerializer(data=request.data)
    if ser.is_valid():
        return Response(data={"message":"collection created"})
    return Response(data={"message":"failed to create collection"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(["GET"])
def get_collections(request):
    query = SongCollection.objects.all()
    ser = SongCollectionSerializer(query, many=True)
    return Response(data=ser.data)

@api_view(["PUT"])
def add_songs(request):
    coll_id = request.data["id"]
    songs = request.data["songs"]
    songs_q = SongLyrics.objects.filter(name__in=songs)

    try:
        coll = SongCollection.objects.get(id=coll_id)
        coll.songs.add(*songs_q) ## using * to unpack the queryset
        
        return Response(data={"message":"song added"})
    except Exception as e:
        print(e)
        return Response(data={"message":str(e)}, status=status.HTTP_404_NOT_FOUND)

    
    