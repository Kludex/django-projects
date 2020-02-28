from django.db import models


class City(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not City.objects.filter(name=self.name).exists():
            super(City, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Cities'
