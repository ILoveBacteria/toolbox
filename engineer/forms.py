from django import forms


class FileForm(forms.Form):
    file = forms.FileField()

    def clean_file(self):
        file = self.cleaned_data['file']
        if file.content_type != 'text/html':
            raise forms.ValidationError('File must be text/html')
        return file
