import datetime
# import uuid

from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from releases.models import Release, Track, Link


class ReleaseViewTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        ok = Release.objects.create(
            release_type="LP",
            title="OK Computer",
            slug="ok-computer",
            pub_datetime=timezone.now(),
            release_date=datetime.date.today())
        Track.objects.create(
            release=ok,
            title="No Surprises",
            length=datetime.timedelta(minutes=3))
        Link.objects.create(release=ok, url="www.google.com", name="Google")

    def test_view_queryset_includes_release(self):
        rels = Release.published.all()
        self.assertEqual(len(rels), 1)

    def test_release_is_published(self):
        # rel = Release.objects.get(id=1)
        rel = Release.objects.get(title="OK Computer")
        self.assertTrue(rel.is_published)

    def test_list_contains_release(self):
        # rel = Release.objects.get(id=1)
        rel = Release.objects.get(title="OK Computer")
        response = self.client.get(reverse('releases:index'))
        self.assertIn(rel, response.context['release_list'])

    def test_correct_index_template_used_noreverse(self):
        response = self.client.get('/releases/')
        # response = self.client.get(reverse('releases:index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'releases/index.html')

    def test_correct_index_template_used(self):
        response = self.client.get(reverse('releases:index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'releases/index.html')

    def test_correct_detail_template_used_noreverse(self):
        expected_url = '/releases/ok-computer/'
        response = self.client.get(expected_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'releases/detail.html')

    def test_correct_detail_template_used(self):
        rel = Release.objects.get(title="OK Computer")
        response = self.client.get(
            reverse('releases:detail', kwargs={'slug': rel.slug}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'releases/detail.html')

    def test_404_on_missing_release(self):
        response = self.client.get(
            reverse('releases:detail', kwargs={'slug': 'kid-a'}))
        self.assertEqual(response.status_code, 404)

    def test_releases_active_in_context(self):
        response = self.client.get(reverse('releases:index'))
        self.assertTrue(response.context['releases_active'])
