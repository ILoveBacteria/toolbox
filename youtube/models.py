import os
from django.db import models


class Playlist(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Video(models.Model):
    # TODO: On delete -> delete files
    # TODO: Change fields type
    DOWNLOAD_STATUS = (
        ('D', 'Downloading'),
        ('C', 'Complete'),
        ('F', 'Fail'),
    )
    title = models.CharField(max_length=255)
    status = models.CharField(choices=DOWNLOAD_STATUS, max_length=255, default='D')
    saved_path = models.CharField(max_length=255, null=True)
    download_url = models.CharField(max_length=255, null=True)
    playlist = models.ForeignKey('Playlist', on_delete=models.CASCADE, null=True)

    def delete(self, *args, **kwargs):
        if os.path.exists(self.saved_path):
            os.remove(self.saved_path)
        super().delete(*args, **kwargs)

    def __str__(self):
        return self.title
