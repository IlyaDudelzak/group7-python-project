"""Forms for the files app."""

from django import forms

class UploadFileForm(forms.Form):
    """
    Form for uploading a file.

    Fields:
        file: The file to be uploaded.
    """
    file = forms.FileField(label="")