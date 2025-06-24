from django import forms


class ChatMessageForm(forms.Form):
    message = forms.CharField(widget=forms.Textarea, required=True)