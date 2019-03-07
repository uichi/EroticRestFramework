import django_filters
from rest_framework import filters, generics, viewsets
from .models import Actresses, Genres, Videos
from .serializer import ActressesSerializer, GenresSerializer, VideosSerializer

class ActressesViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Actresses.objects.all()
    serializer_class = ActressesSerializer
    filter_fields = ('name',)

class GenresViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Genres.objects.all()
    serializer_class = GenresSerializer
    filter_fields = ('name',)

class VideosViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Videos.objects.all()
    serializer_class = VideosSerializer
    filter_fields = ('actress', 'genre')