"""Models for the chat application."""

from django.db import models
from django.utils import timezone


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

    class Meta:
        ordering = ['timestamp']

    def __str__(self):
        """String representation of ChatMessage."""
        return f"{self.role}: {self.content[:50]}..."
