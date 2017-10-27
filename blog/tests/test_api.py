from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

import datetime

from blog.models import Blog


class BlogAPITests(TestCase):
    @classmethod
    def setUpTestData(cls):
        Blog.objects.create(
            title="Today",
            text="Today's News",
            pub_datetime=timezone.now(),
            slug="today")
        Blog.objects.create(
            title="Tomorrow",
            text="Tomorrow's News",
            pub_datetime=(timezone.now() + datetime.timedelta(days=1)),
            slug="tomorrow")

    def test_list(self):
        response = self.client.get(reverse('api:blog-list'))
        self.assertEquals(response.status_code, 200)
        self.assertContains(response, "Today")
        self.assertNotContains(response, "Tomorrow")

    def test_detail(self):
        response = self.client.get(
            reverse('api:blog-detail', kwargs={'slug': 'today'}))
        self.assertEquals(response.status_code, 200)
        self.assertContains(response, "Today")
