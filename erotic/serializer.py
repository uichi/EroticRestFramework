from rest_framework import serializers
from .models import Actresses, Genres, Videos

class ActressesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actresses
        fields = ('id', 'name')


class GenresSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genres
        fields = ('id', 'name')

class VideosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Videos
        fields = ('actress', 'genre', 'title', 'description', 'url')