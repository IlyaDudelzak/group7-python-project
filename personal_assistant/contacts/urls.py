from django.urls import path
from .views import contacts_view, create_contact

app_name = 'contacts'

urlpatterns = [
    path('', contacts_view, name='contact_view'),
    path('create/', create_contact, name='create_contact'),
]