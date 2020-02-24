from django.db import models
from django.urls import reverse

class Paste(models.Model):
    text = models.TextField()
    name = models.CharField(max_length=40, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name or str(self.id)

    def get_absolute_url(self):
        return reverse('paste_detail', args=[self.id])
