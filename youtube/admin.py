from django.contrib import admin
from .models import VideoModel, PlaylistModel


@admin.register(VideoModel)
class VideoAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'playlist')


@admin.register(PlaylistModel)
class PlaylistAdmin(admin.ModelAdmin):
    list_display = ('title', 'count_videos')

    def count_videos(self, obj: PlaylistModel):
        return obj.videomodel_set.count()
