from django.shortcuts import render, HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import *
from pytube import YouTube, Playlist
from server_admin.config_loader import config
import threading
from .models import VideoModel, PlaylistModel


@login_required
def video(request):
    if request.method == "POST":
        form = DownloadVideoForm(request.POST)
        if form.is_valid():
            link = form.cleaned_data['link']
            threading.Thread(target=download_video, args=(link,)).start()
            return HttpResponse('Download in progress...')
        return render(
            request,
            'youtube/download_video.html',
            context={'form': form, 'title': 'Download Video'},
            status=400,
        )
    else:
        form = DownloadVideoForm()
        return render(request, 'youtube/download_video.html', context={'form': form, 'title': 'Download Video'})


@login_required
def playlist(request):
    if request.method == "POST":
        form = DownloadPlaylistForm(request.POST)
        if form.is_valid():
            threading.Thread(
                target=download_playlist,
                args=(
                    form.cleaned_data['link'],
                    form.cleaned_data['from_episode'],
                    form.cleaned_data['to_episode'],
                )
            ).start()
            return HttpResponse('Download in progress...')
        return render(
            request,
            'youtube/download_playlist.html',
            context={'form': form, 'title': 'Download Playlist'},
            status=400,
        )
    else:
        form = DownloadPlaylistForm()
        return render(request, 'youtube/download_playlist.html', context={'form': form, 'title': 'Download Playlist'})


def download_video(url: str):
    # TODO: Log correctly
    # TODO: Fail handling here and on the forms
    v = YouTube(url)
    video_instance = VideoModel.objects.create(title=v.title)
    destination_saved_path = v \
        .streams \
        .get_highest_resolution() \
        .download(output_path=f'{config["FILE_SERVER"]}/youtube/videos')
    video_instance.status = 'C'
    video_instance.saved_path = destination_saved_path
    video_instance.save()


def download_playlist(url: str, from_episode: int, to_episode: int):
    p = Playlist(url)
    playlist_instance = PlaylistModel.objects.create(title=p.title)
    for url in list(p)[from_episode - 1:to_episode]:
        v = YouTube(url)
        video_instance = playlist_instance.videomodel_set.create(title=v.title)
        destination_saved_path = v.streams \
            .get_highest_resolution() \
            .download(output_path=f'{config["FILE_SERVER"]}/youtube/playlists/{p.title}')
        video_instance.status = 'C'
        video_instance.saved_path = destination_saved_path
        video_instance.save()

# TODO: track last updated videos and download them
