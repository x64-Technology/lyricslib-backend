from rest_framework.response import Response
from .serializer import SongCollectionSerializer, SongCollectionSerializerPart, SongForHome
from .models import SongCollection, SongLyric
from rest_framework.decorators import api_view
from rest_framework import status

@api_view(["POST"])
def create_collection(request):
    ser = SongCollectionSerializer(data=request.data)
    try:
        if ser.is_valid(raise_exception=True):
            ser.save()
            return Response(data={"message":"collection created"})
    except Exception as e:
        return Response(data={"message":str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(["GET"])
def get_collections(request):
    query = SongCollection.objects.all()
    ser = SongCollectionSerializerPart(query, many=True)
    return Response(data=ser.data)

@api_view(["GET"])
def get_collection(request, id:int):
    try:
        query = SongCollection.objects.get(id=id)
        context = SongCollectionSerializer(query).data

        songs = SongLyric.objects.filter(songcollection__id=id)
        context["songs"] = SongForHome(songs, many=True).data
        return Response(data=context)
    except Exception as e:
        return Response(data={"message":str(e)}, status=status.HTTP_404_NOT_FOUND)
    
@api_view(["PUT"])
def add_songs(request):
    coll_id = request.data["id"]
    songs = request.data["songs"]
    songs_q = SongLyric.objects.filter(name__in=songs)

    try:
        coll = SongCollection.objects.get(id=coll_id)
        coll.songs.add(*songs_q) ## using * to unpack the queryset
        
        return Response(data={"message":"song added"})
    except Exception as e:
        print(e)
        return Response(data={"message":str(e)}, status=status.HTTP_404_NOT_FOUND)

    
    