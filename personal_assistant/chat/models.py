"""Models for the chat application."""

from django.db import models
from django.utils import timezone
from django.conf import settings


class ChatMessage(models.Model):
    """
    Model to store chat messages between user and AI.
    """
    ROLE_CHOICES = [
        ('user', 'User'),
        ('assistant', 'Assistant'),
    ]

    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    content = models.TextField()
    timestamp = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.CASCADE)
    device_key = models.CharField(max_length=64, null=True, blank=True)

    class Meta:
        ordering = ['timestamp']

    def __str__(self):
        """String representation of ChatMessage."""
        return f"{self.role}: {self.content[:50]}..."
