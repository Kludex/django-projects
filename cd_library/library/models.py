from django.db import models


GENRE_CHOICES = (
    ('R', 'ROCK'),
    ('B', 'BLUES'),
    ('J', 'JAZZ'),
    ('P', 'POP'),
)

class CD(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    artist = models.CharField(max_length=40)
    date = models.DateField()
    genre = models.CharField(max_length=1, choices=GENRE_CHOICES)

    def __str__(self):
        return "{} by {}, {}".format(self.title, self.artist, self.date.year)
