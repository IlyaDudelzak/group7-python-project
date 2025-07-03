"""
Models for user profile extension.
"""

from django.db import models
from django.contrib.auth.models import User
from PIL import Image

User._meta.get_field('email')._unique = True


class Profile(models.Model):
    """User profile model extending the default User with an avatar."""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(default='default_avatar.png', upload_to='profile_images')

    def __str__(self):
        """Return the username as string representation."""
        return self.user.username

    def save(self, *args, **kwargs):
        """Override save to resize avatar image if needed."""
        super().save()

        img = Image.open(self.avatar.path)

        if img.height > 250 or img.width > 250:
            new_img = (250, 250)
            img.thumbnail(new_img)
            img.save(self.avatar.path)