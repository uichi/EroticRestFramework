from django.urls import path, include
from rest_framework import routers
from .views import ActressesViewSet, GenresViewSet, VideosViewSet

router = routers.DefaultRouter()
router.register(r'actresses', ActressesViewSet)
router.register(r'genres', GenresViewSet)
router.register(r'videos', VideosViewSet)

urlpatterns = [
    path('', include(router.urls)),
]