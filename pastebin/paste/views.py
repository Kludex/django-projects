from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic import DeleteView
from django.urls import reverse, reverse_lazy
from .models import Paste

class PasteCreate(CreateView):
    model = Paste
    fields = ['text', 'name']

class PasteDetail(DetailView):
    model = Paste
    template_name = "paste/paste_detail.html"

class PasteList(ListView):
    model = Paste
    template_name = 'paste/paste_list.html'

class PasteEdit(UpdateView):
    model = Paste
    fields = ['text', 'name']

class PasteDelete(DeleteView):
    model = Paste
    success_url = reverse_lazy('paste_list')
