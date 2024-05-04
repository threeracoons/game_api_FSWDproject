#________________________

from django.contrib import admin
from .models import VideoGame

@admin.register(VideoGame)
class VideoGameAdmin(admin.ModelAdmin):
    list_display = ('title', 'platform', 'genre', 'release_date', 'price')
