from django.shortcuts import render, HttpResponse
from .forms import *


def download_video(request):
    if request.method == "POST":
        form = DownloadVideoForm(request.POST)
        if form.is_valid():
            return HttpResponse(form.cleaned_data['link'])
        return render(request, 'youtube/download_video.html', context={'form': form}, status=400)
    else:
        form = DownloadVideoForm()
        return render(request, 'youtube/download_video.html', context={'form': form})


def download_playlist(request):
    if request.method == "POST":
        form = DownloadPlaylistForm(request.POST)
        if form.is_valid():
            return HttpResponse('thankyou')
        return render(request, 'youtube/download_playlist.html', context={'form': form}, status=400)
    else:
        form = DownloadPlaylistForm()
        return render(request, 'youtube/download_playlist.html', context={'form': form})
