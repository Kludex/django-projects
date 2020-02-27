from django.urls import path

from .views import NoteListView, NoteDeleteView

urlpatterns = [
    path('', NoteListView.as_view(), name='note-list'),
    path('remove/<int:pk>', NoteDeleteView.as_view(), name='note-delete'),
]