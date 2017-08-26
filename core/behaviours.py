from django.db import models
from django.utils import timezone


# Create your models here.
class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset().filter(
            pub_datetime__lte=timezone.now())

    # use_for_related_fields = True

    # def published(self, **kwargs):
    #     return self.filter(pub_datetime__lte=timezone.now(), **kwargs)


class Publishable(models.Model):
    publish_date = models.DateTimeField(null=True)

    class Meta:
        abstract = True

    def publish_on(self, date=timezone.now()):
        self.publish_date = date
        self.save()

    @property
    def is_published(self):
        return self.publish_date < timezone.now()
