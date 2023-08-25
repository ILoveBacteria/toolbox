from django.shortcuts import render, HttpResponse
from .forms import DownloadVideoForm


def download_video(request):
    if request.method == "POST":
        form = DownloadVideoForm(request.POST)
        if form.is_valid():
            return HttpResponse(form.cleaned_data['link'])
        return render(request, 'youtube/download_video.html', context={'form': form}, status=400)
    else:
        form = DownloadVideoForm()
        return render(request, 'youtube/download_video.html', context={'form': form})
