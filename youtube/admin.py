from django.contrib import admin, messages
from .models import Video, Playlist


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'playlist')
    actions = ['delete_with_video_file']

    @admin.action
    def delete_with_video_file(self, request, queryset):
        for obj in queryset:
            obj.delete()
        self.message_user(request, 'Successfully delete with videos', messages.SUCCESS)


@admin.register(Playlist)
class PlaylistAdmin(admin.ModelAdmin):
    list_display = ('title', 'count_videos')

    def count_videos(self, obj: Playlist):
        return obj.video_set.count()
