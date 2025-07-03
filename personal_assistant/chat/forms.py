"""
Forms for the chat app.
"""

from django import forms


class ChatMessageForm(forms.Form):
    """Form for submitting a chat message."""

    message = forms.CharField(widget=forms.Textarea, required=True)