from django.forms import ModelForm, CharField, EmailField, TextInput
from phonenumber_field.formfields import PhoneNumberField
from .models import Contact


class ContactForm(ModelForm):
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