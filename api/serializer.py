from rest_framework import serializers
from .models import SongLyric, SongCollection

class SongForHome(serializers.ModelSerializer):

    class Meta:
        model = SongLyric
        fields = ['id', 'name', 'album', 'image']

class SongLyricsSerializer(serializers.ModelSerializer):

    class Meta:
        model = SongLyric
        fields = "__all__"

class SearchSongLyricsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = SongLyric
        fields = ['id', 'name', 'album', 'singer', 'image']

class SongCollectionSerializerPart(serializers.ModelSerializer):
    class Meta:
        model = SongCollection
        fields = ['id', 'title', 'image']

class SongCollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = SongCollection
        fields = '__all__'