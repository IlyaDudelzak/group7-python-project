from django.urls import path
from .views import notes_view, tag, note, detail, edit_note, delete_note

app_name = 'notes'

urlpatterns = [
    path("", notes_view, name="notes"),
    path('note/', note, name='note'),
    path('tag/', tag, name='tag'),
    path('detail/<int:note_id>', detail, name='detail'),
    path('edit/<int:note_id>/', edit_note, name='edit'),
    path('delete/<int:note_id>', delete_note, name='delete'),
]