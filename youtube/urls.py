from django.urls import path
from .views import DownloadPlaylistView, DownloadVideoView, PlaylistDetailView, PlaylistListView, VideoDetailView, VideoListView


urlpatterns = [
    path('playlist/', DownloadPlaylistView.as_view(), name='playlist'),
    path('playlists/<int:pk>', PlaylistDetailView.as_view(), name='playlist_detail'),
    path('playlists/', PlaylistListView.as_view(), name='playlist_list'),
    path('video/', DownloadVideoView.as_view(), name='video'),
    path('videos/', VideoListView.as_view(), name='video_list'),
    path('videos/<int:pk>', VideoDetailView.as_view(), name='video_detail'),
]
