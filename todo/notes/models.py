from django.db import models


class Note(models.Model):
    text = models.CharField(max_length=40)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.id
