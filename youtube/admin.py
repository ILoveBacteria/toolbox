import pathlib
import zipfile
import datetime
from django.contrib import admin, messages
from .models import Video, Playlist
from server_admin.config_loader import config


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'playlist')
    actions = ['delete_with_video_file', 'zip_files']

    @admin.action
    def delete_with_video_file(self, request, queryset):
        for obj in queryset:
            obj.delete()
        self.message_user(request, 'Successfully delete with videos', messages.SUCCESS)

    @admin.action
    def zip_files(self, request, queryset):
        now = datetime.datetime.now()
        zip_name = now.strftime('%y-%m-%d_%H-%M-%S')
        path = pathlib.Path(config['FILE_SERVER'], 'archives', f'{zip_name}.zip')
        with zipfile.ZipFile(path, 'w') as archive:
            for obj in queryset:
                archive.write(obj.saved_path)
        self.message_user(request, 'Successfully archived', messages.SUCCESS)


@admin.register(Playlist)
class PlaylistAdmin(admin.ModelAdmin):
    list_display = ('title', 'count_videos')

    def count_videos(self, obj: Playlist):
        return obj.video_set.count()
