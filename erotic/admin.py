from django.contrib import admin
from .models import Actresses, Genres, Videos

@admin.register(Actresses)
class Actresses(admin.ModelAdmin):
    pass

@admin.register(Genres)
class Genres(admin.ModelAdmin):
    pass

@admin.register(Videos)
class Videos(admin.ModelAdmin):
    pass