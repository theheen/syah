import datetime
# import uuid

from django.db import models
from django.utils import timezone
from django.core.urlresolvers import reverse
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFit

from core.behaviours import PublishedManager

# Create your models here.


class Release(models.Model):
    ALBUM = 'LP'
    EP = 'EP'
    SINGLE = 'SN'
    COMPILATION = 'CM'
    LIVE = 'LV'
    RELEASE_TYPE_CHOICES = ((ALBUM, 'Album'), (EP, 'EP'), (SINGLE, 'Single'),
                            (COMPILATION, 'Compilation'), (LIVE, 'Live'), )
    release_type = models.CharField(
        max_length=2,
        choices=RELEASE_TYPE_CHOICES,
        default=ALBUM, )
    release_date = models.DateField(
        default=datetime.date.today,
        help_text="When the release is available to the public.")
    pub_datetime = models.DateTimeField(
        default=timezone.now,
        help_text="When the release will be made visible on-site.")
    title = models.CharField(max_length=500)
    slug = models.SlugField(unique=True)
    tagline = models.CharField(max_length=200, default='', blank=True)
    info = models.TextField(default='', blank=True)
    cover = models.ImageField(upload_to='covers', default='missing.gif')
    cover_thumb_300 = ImageSpecField(
        source='cover', processors=[ResizeToFit(300, 300)])
    cover_thumb_550 = ImageSpecField(
        source='cover', processors=[ResizeToFit(550, 550)])

    objects = models.Manager()
    published = PublishedManager()

    def __str__(self):
        return self.title

    @property
    def is_released(self):
        return self.release_date <= timezone.now().date()

    @property
    def is_published(self):
        return self.pub_datetime <= timezone.now()

    def get_absolute_url(self):
        return reverse('releases:detail', kwargs={'slug': self.slug})
        # return reverse(
        #     'releases:detail', kwargs={'pk': self.id,
        #                                'slug': self.slug})


class Track(models.Model):
    release = models.ForeignKey(Release, on_delete=models.CASCADE)
    title = models.CharField(max_length=300)
    length = models.DurationField()

    def __str__(self):
        return self.title


class Link(models.Model):
    release = models.ForeignKey(Release, on_delete=models.CASCADE)
    url = models.URLField()
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name
