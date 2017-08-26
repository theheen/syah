from django.db import models
from django.utils import timezone
from django.core.urlresolvers import reverse

from core.behaviours import PublishedManager


# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    pub_datetime = models.DateTimeField(default=timezone.now)
    # mod_date = models.DateField(auto_now=True)
    slug = models.SlugField(unique=True)
    objects = models.Manager()
    published = PublishedManager()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'slug': self.slug})

    @property
    def is_published(self):
        return timezone.now() > self.pub_datetime
