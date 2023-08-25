from django.urls import path
from .views import *

urlpatterns = [
    path('video/', download_video, name="download_video")
]