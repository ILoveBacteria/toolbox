from django.urls import path
from .views import *

urlpatterns = [
    path('video/', DownloadVideoView.as_view(), name='video'),
    # path('videos/<int:id>', VideoDetailView.as_view(), name='video_detail'),
    path('playlist/', playlist, name='playlist')
]
