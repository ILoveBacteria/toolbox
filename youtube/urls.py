from django.urls import path

from youtube import views


urlpatterns = [
    path('playlist/', views.DownloadPlaylistView.as_view(), name='playlist'),
    path('playlists/update/<int:pk>', views.PlaylistUpdateView.as_view(), name='playlist_update'),
    path('playlists/<int:pk>', views.PlaylistDetailView.as_view(), name='playlist_detail'),
    path('playlists/', views.PlaylistListView.as_view(), name='playlist_list'),
    path('video/', views.DownloadVideoView.as_view(), name='video'),
    path('videos/', views.VideoListView.as_view(), name='video_list'),
    path('videos/delete/<int:pk>', views.VideoDeleteView.as_view(), name='video_delete'),
    path('videos/update/<int:pk>', views.VideoUpdateView.as_view(), name='video_update'),
    path('videos/<int:pk>', views.VideoDetailView.as_view(), name='video_detail'),
]
