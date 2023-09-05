from django.contrib import admin
from .models import Video, Playlist


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'playlist')


@admin.register(Playlist)
class PlaylistAdmin(admin.ModelAdmin):
    list_display = ('title', 'count_videos')

    def count_videos(self, obj: Playlist):
        return obj.video_set.count()
