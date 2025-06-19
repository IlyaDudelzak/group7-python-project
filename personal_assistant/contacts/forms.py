"""Forms for the contacts app."""

from django.forms import ModelForm, CharField, EmailField, TextInput
from phonenumber_field.formfields import PhoneNumberField
from .models import Contact


class ContactForm(ModelForm):
    """
    Form for creating and editing Contact instances.

    Fields:
        first_name: The contact's first name.
        last_name: The contact's last name.
        address: The contact's address.
        email: The contact's email address.
        phone_number: The contact's phone number.
        birthday: The contact's birthday.
    """

    first_name = CharField(
        min_length=2,
        max_length=150,
        required=True,
    )
    last_name = CharField(
        min_length=2,
        max_length=150,
        required=True,
    )
    address = CharField(
        max_length=150,
        required=False,
    )
    email = EmailField(
        max_length=150,
        required=True,
    )
    phone_number = PhoneNumberField(
        required=True,
        widget=TextInput(attrs={'placeholder': '+380xxxxxxxxx'})
    )
    birthday = CharField(
        max_length=50,
        required=False,
        widget=TextInput(attrs={'placeholder': 'YYYY-MM-DD'})
    )

    class Meta:
        model = Contact
        fields = ['first_name', 'last_name', 'address', 'email', 'phone_number', 'birthday']