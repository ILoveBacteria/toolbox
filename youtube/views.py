import threading

from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import HttpResponse
from django.views.generic import FormView
from pytube import YouTube, Playlist

from server_admin.config_loader import config
from .forms import DownloadVideoForm, DownloadPlaylistForm
from .models import Playlist as PlaylistModel
from .models import Video


class DownloadVideoView(LoginRequiredMixin, FormView):
    form_class = DownloadVideoForm
    template_name = 'form.html'

    def form_valid(self, form):
        link = form.cleaned_data['link']
        threading.Thread(target=download_video, args=(link,)).start()
        return HttpResponse('Download in progress...')


class DownloadPlaylistView(LoginRequiredMixin, FormView):
    form_class = DownloadPlaylistForm
    template_name = 'form.html'

    def form_valid(self, form):
        threading.Thread(
            target=download_playlist,
            args=(
                form.cleaned_data['link'],
                form.cleaned_data['from_episode'],
                form.cleaned_data['to_episode'],
            )
        ).start()
        return HttpResponse('Download in progress...')


# class VideoDetailView(DetailView):
#     model = Video

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context["now"] = timezone.now()
    #     return context


def download_video(url: str):
    # TODO: Log correctly
    # TODO: Fail handling here and on the forms
    v = YouTube(url)
    video_instance = Video.objects.create(title=v.title)
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
        video_instance = playlist_instance.video_set.create(title=v.title)
        destination_saved_path = v.streams \
            .get_highest_resolution() \
            .download(output_path=f'{config["FILE_SERVER"]}/youtube/playlists/{p.title}')
        video_instance.status = 'C'
        video_instance.saved_path = destination_saved_path
        video_instance.save()

# TODO: track last updated videos and download them
