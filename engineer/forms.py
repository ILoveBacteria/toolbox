from django import forms
from engineer.models import Vocabulary


class VocabForm(forms.ModelForm):
    class Meta:
        model = Vocabulary
        fields = ['word', 'example', 'translation']


class FileForm(forms.Form):
    file = forms.FileField()

    def clean_file(self):
        file = self.cleaned_data['file']
        if file.content_type != 'text/html':
            raise forms.ValidationError('File must be text/html')
        return file
