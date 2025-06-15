from django.db import models

# Create your models here.


class Contact(models.Model):
    first_name = models.CharField(max_length=150, null=False)
    last_name = models.CharField(max_length=150, null=False)
    address = models.CharField(max_length=150)
    email = models.EmailField(max_length=150, unique=True)
    phone_number = models.CharField(max_length=30, unique=True)
    birthday = models.CharField(max_length=50)
    created_at=models.DateTimeField(auto_now_add=True)

