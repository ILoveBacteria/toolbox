import re
import threading
import environ

from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import DetailView, FormView, ListView, UpdateView, DeleteView
from pytube import YouTube, Playlist

from .forms import DownloadVideoForm, DownloadPlaylistForm
from .models import Playlist as PlaylistModel
from .models import Video


env = environ.Env()


class DownloadVideoView(LoginRequiredMixin, FormView):
    form_class = DownloadVideoForm
    template_name = 'form.html'
    extra_context = {'title': 'Download Video'}

    def form_valid(self, form):
        link = form.cleaned_data['link']
        threading.Thread(target=download_video, args=(link,)).start()
        return HttpResponse('Download in progress...')


class DownloadPlaylistView(LoginRequiredMixin, FormView):
    form_class = DownloadPlaylistForm
    template_name = 'form.html'
    extra_context = {'title': 'Download Playlist'}

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


class PlaylistDetailView(LoginRequiredMixin, DetailView):
    model = PlaylistModel

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs, title=f"Playlist {self.kwargs['pk']}")


class PlaylistUpdateView(LoginRequiredMixin, UpdateView):
    model = PlaylistModel
    fields = '__all__'
    template_name = 'form.html'

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs, title=f"Playlist {self.kwargs['pk']}")


class PlaylistListView(LoginRequiredMixin, ListView):
    model = PlaylistModel
    extra_context = {'title': 'Playlists'}


class VideoDeleteView(DeleteView):
    model = Video
    success_url = reverse_lazy('video_list')

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs, title=f"Video {self.kwargs['pk']}")


class VideoDetailView(LoginRequiredMixin, DetailView):
    model = Video

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs, title=f"Video {self.kwargs['pk']}")


class VideoUpdateView(LoginRequiredMixin, UpdateView):
    model = Video
    fields = '__all__'
    template_name = 'form.html'

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs, title=f"Video {self.kwargs['pk']}")


class VideoListView(LoginRequiredMixin, ListView):
    model = Video
    extra_context = {'title': 'Videos'}


def download_video(url: str):
    # TODO: Log correctly
    # TODO: Fail handling here and on the forms
    v = YouTube(url)
    video_instance = Video.objects.create(title=v.title)
    destination_saved_path = v \
        .streams \
        .get_highest_resolution() \
        .download(output_path=f'{env("FILE_SERVER")}/youtube/videos')
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
            .download(output_path=f'{env("FILE_SERVER")}/youtube/playlists/{directory_name_cleaner(p.title)}')
        video_instance.status = 'C'
        video_instance.saved_path = destination_saved_path
        video_instance.save()


def directory_name_cleaner(name: str):
    return re.sub('[<>:\"/?|*]', '', name)

# TODO: track last updated videos and download them
