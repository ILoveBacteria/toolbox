from django.urls import path
from .views import *

urlpatterns = [
    path('video/', download_video, name='download_video'),
    path('playlist/', download_playlist, name='download_playlist')
]
