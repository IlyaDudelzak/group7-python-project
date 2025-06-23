"""This file registers the Contact model with the Django admin site."""

from django.contrib import admin
from .models import Contact

# Register your models here.
admin.site.register(Contact)
