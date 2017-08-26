from django.db import models


# Create your models here.
class Venue(models.Model):
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=70)
    url = models.URLField(blank=True)

    def __str__(self):
        return self.name


class Event(models.Model):
    venue = models.ForeignKey(Venue, on_delete=models.CASCADE)
    date = models.DateField()
    ticket_url = models.URLField(blank=True)
    info = models.TextField(blank=True, default='')

    def __str__(self):
        return '%s: %s' % (str(self.date), self.venue.name)
