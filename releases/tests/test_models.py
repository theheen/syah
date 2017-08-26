import datetime

from django.test import TestCase
from django.utils import timezone

from releases.models import Release, Track, Link


# Create your tests here.
class ReleaseModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        ok = Release.objects.create(
            release_type='LP', title="OK Computer", slug="ok-computer")
        Release.objects.create(
            release_type='LP',
            release_date=(
                datetime.date.today() + datetime.timedelta(days=365)),
            pub_datetime=(timezone.now() + datetime.timedelta(days=365)),
            title="Kid A",
            slug="kid-a")
        Release.objects.create(
            release_type='EP', title="Slug Challenge", slug="-_123abc")
        Track.objects.create(
            release=ok,
            title="No Surprises",
            length=datetime.timedelta(minutes=4))
        Link.objects.create(
            release=ok, url="www.radiohead.com", name="Radiohead")

    def test_release_str(self):
        # rel = Release.objects.get(id=1)
        rel = Release.objects.get(title="OK Computer")
        self.assertEqual(str(rel), "OK Computer")

    def test_is_published(self):
        # pub = Release.objects.get(id=1)
        pub = Release.objects.get(title="OK Computer")
        self.assertTrue(pub.is_published)
        # not_pub = Release.objects.get(id=2)
        not_pub = Release.objects.get(title="Kid A")
        self.assertFalse(not_pub.is_published)

    def test_is_released(self):
        # rel = Release.objects.get(id=1)
        rel = Release.objects.get(title="OK Computer")
        self.assertTrue(rel.is_released)
        # not_rel = Release.objects.get(id=2)
        not_rel = Release.objects.get(title="Kid A")
        self.assertFalse(not_rel.is_released)

    def test_absolute_url(self):
        # rel = Release.objects.get(id=1)
        rel = Release.objects.get(title="OK Computer")
        expected = '/releases/{0}/'.format(rel.slug)
        self.assertEqual(rel.get_absolute_url(), expected)
        # outlier = Release.objects.get(id=3)
        outlier = Release.objects.get(title="Slug Challenge")
        outlier_expected = '/releases/{0}/'.format(outlier.slug)
        self.assertEqual(outlier.get_absolute_url(), outlier_expected)

    def test_track_str(self):
        # track = Track.objects.get(id=1)
        track = Track.objects.get(title="No Surprises")
        self.assertEqual(str(track), "No Surprises")

    def test_link_str(self):
        # link = Link.objects.get(id=1)
        link = Link.objects.get(name="Radiohead")
        self.assertEqual(str(link), "Radiohead")
