from django.urls import path
from .views import *

urlpatterns = [
    path('video/', video, name='video'),
    path('playlist/', playlist, name='playlist')
]
