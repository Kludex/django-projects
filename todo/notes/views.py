from django.shortcuts import render, redirect, reverse
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic import DeleteView

from .models import Note


class NoteListView(ListView):
    model = Note

    def get_context_data(self, *args, **kwargs):
        content = {}
        content['notes'] = Note.objects.all()
        return content

    def post(self, request, *args, **kwargs):
        text = request.POST.get('text')
        if text:
            note = Note(text=text)
            note.save()
        return redirect(reverse('note-list'))

class NoteDeleteView(DeleteView):
    model = Note
    success_url = reverse_lazy('note-list')
