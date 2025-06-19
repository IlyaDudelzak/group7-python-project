"""Models for the contacts app."""

from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.


class Contact(models.Model):
    """
    Model representing a contact entry.

    Fields:
        first_name (str): The contact's first name.
        last_name (str): The contact's last name.
        address (str): The contact's address.
        email (str): The contact's email address.
        phone_number (PhoneNumberField): The contact's phone number.
        birthday (date): The contact's birthday.
        created_at (datetime): The date and time the contact was created.
    """

    first_name = models.CharField(max_length=150, null=False)
    last_name = models.CharField(max_length=150, null=False)
    address = models.CharField(max_length=150)
    email = models.EmailField(max_length=150, unique=True)
    phone_number = PhoneNumberField(unique=True)
    birthday = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

