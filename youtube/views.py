from django.shortcuts import render, HttpResponse
from .forms import *
from pytube import YouTube, Playlist
import threading


# TODO: Login required
def video(request):
    if request.method == "POST":
        form = DownloadVideoForm(request.POST)
        if form.is_valid():
            link = form.cleaned_data['link']
            threading.Thread(target=download_video, args=(link,)).start()
            return HttpResponse('Download in progress...')
        return render(request, 'youtube/download_video.html', context={'form': form}, status=400)
    else:
        form = DownloadVideoForm()
        return render(request, 'youtube/download_video.html', context={'form': form})


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
        return render(request, 'youtube/download_playlist.html', context={'form': form}, status=400)
    else:
        form = DownloadPlaylistForm()
        return render(request, 'youtube/download_playlist.html', context={'form': form})


def download_video(url: str):
    YouTube(url) \
        .streams \
        .get_highest_resolution() \
        .download(output_path='youtube/downloads/videos')


def download_playlist(url: str, from_episode: int, to_episode: int):
    p = Playlist(url)
    for url in list(p)[from_episode:to_episode + 1]:
        YouTube(url).streams \
            .get_highest_resolution() \
            .download(output_path=f'youtube/downloads/playlists/{p.title}')

# TODO: track last updated videos and download them
