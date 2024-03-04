from rest_framework import serializers
from .models import SongLyrics, SongCollection

class SongLyricsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SongLyrics
        fields = '__all__'

class SearchSongLyricsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SongLyrics
        fields = ['id', 'name', 'album', 'singer', 'image']


class SongCollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = SongCollection
        fields = '__all__'