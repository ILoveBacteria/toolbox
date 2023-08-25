from django import forms


class DownloadVideoForm(forms.Form):
    link = forms.URLField()

