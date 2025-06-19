from django.db import models

# Create your models here.

from django.contrib.auth.models import User


class UploadedFile(models.Model):
    filename = models.CharField(max_length=255)
    url = models.TextField()
    uploaded_at = models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length=20, choices=[
        ("image", "Image"),
        ("document", "Document"),
        ("video", "Video"),
        ("other", "Other"),
    ])
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.filename
