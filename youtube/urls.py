from django.urls import path
from .views import DownloadPlaylistView, DownloadVideoView, PlaylistDetailView, PlaylistListView, VideoDetailView, \
    VideoListView, VideoUpdateView, PlaylistUpdateView, VideoDeleteView

urlpatterns = [
    path('playlist/', DownloadPlaylistView.as_view(), name='playlist'),
    path('playlists/update/<int:pk>', PlaylistUpdateView.as_view(), name='playlist_update'),
    path('playlists/<int:pk>', PlaylistDetailView.as_view(), name='playlist_detail'),
    path('playlists/', PlaylistListView.as_view(), name='playlist_list'),
    path('video/', DownloadVideoView.as_view(), name='video'),
    path('videos/', VideoListView.as_view(), name='video_list'),
    path('videos/delete/<int:pk>', VideoDeleteView.as_view(), name='video_delete'),
    path('videos/update/<int:pk>', VideoUpdateView.as_view(), name='video_update'),
    path('videos/<int:pk>', VideoDetailView.as_view(), name='video_detail'),
]
