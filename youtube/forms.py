from django import forms


class DownloadVideoForm(forms.Form):
    link = forms.URLField(label='Link')


class DownloadPlaylistForm(forms.Form):
    link = forms.URLField(label='Link')
    from_episode = forms.IntegerField(min_value=1, initial=1, label='From')
    to_episode = forms.IntegerField(min_value=1, label='To')
