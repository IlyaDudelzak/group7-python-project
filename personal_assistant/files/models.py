"""Models for the files app."""

from django.db import models

# Create your models here.


# from django.contrib.auth.models import User

class UploadedFile(models.Model):
    """
    Model representing an uploaded file.

    Fields:
        filename (str): The name of the uploaded file.
        url (str): The public URL of the uploaded file.
        uploaded_at (datetime): The date and time the file was uploaded.
        category (str): The category of the file (image, document, video, other).
    """
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    filename = models.CharField(max_length=255)
    url = models.TextField()
    uploaded_at = models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length=20, choices=[
        ("image", "Image"),
        ("document", "Document"),
        ("video", "Video"),
        ("other", "Other"),
    ])

    def __str__(self):
        """Return the filename as string representation."""
        return self.filename
