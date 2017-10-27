import datetime

from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from releases.models import Release


# Create your tests here.
class HomepageViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Release.objects.create(
            release_type='LP', title="OK Computer", slug='ok-computer')
        Release.objects.create(
            release_type='EP',
            title="Kid A",
            slug="kid-a",
            pub_datetime=(timezone.now() + datetime.timedelta(hours=1)))

    def test_homepage_view_at_root_url(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_homepage_url_namespace(self):
        response = self.client.get(reverse('homepage'))
        self.assertEqual(response.status_code, 200)

    def test_homepage_template_used(self):
        response = self.client.get(reverse('homepage'))
        self.assertTemplateUsed(response, 'homepage.html')

    def test_homepage_contains_release(self):
        response = self.client.get(reverse('homepage'))
        self.assertContains(response, "OK Computer")


class CoreBehavioursTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Release.objects.create(
            release_type='LP', title="OK Computer", slug='ok-computer')
        Release.objects.create(
            release_type='EP',
            title="Kid A",
            slug="kid-a",
            pub_datetime=(timezone.now() + datetime.timedelta(hours=1)))
