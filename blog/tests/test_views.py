import datetime

from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from blog.models import Blog


# Create your tests here.
class BlogViewsTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        Blog.objects.create(
            title="Yesterday",
            text="Yesterday's news",
            pub_datetime=(timezone.now() - datetime.timedelta(days=1)),
            slug="yesterday")
        Blog.objects.create(
            title="Today",
            text="Today's news",
            pub_datetime=timezone.now(),
            slug="today")
        Blog.objects.create(
            title="Tomorrow",
            text="Tomorrow's news",
            pub_datetime=(timezone.now() + datetime.timedelta(days=1)),
            slug="tomorrow")

    def test_list_view_exists(self):
        response = self.client.get(reverse('blog:index'))
        self.assertEqual(response.status_code, 200)

    def test_list_view_at_correct_url(self):
        response = self.client.get('/blog/')
        self.assertEqual(response.status_code, 200)

    def test_list_view_uses_correct_template(self):
        response = self.client.get(reverse('blog:index'))
        self.assertTemplateUsed(response, 'blog/index.html')

    def test_detail_view_exists(self):
        blog = Blog.objects.get(title="Yesterday")
        response = self.client.get(
            reverse('blog:detail', kwargs={'slug': blog.slug}))
        self.assertEqual(response.status_code, 200)

    def test_detail_view_at_correct_url(self):
        # blog = Blog.objects.get(title="Yesterday")
        expected_url = '/blog/yesterday/'
        response = self.client.get(expected_url)
        self.assertEqual(response.status_code, 200)

    def test_detail_view_uses_correct_template(self):
        # blog = Blog.objects.get(title="Yesterday")
        response = self.client.get(
            reverse('blog:detail', kwargs={'slug': 'yesterday'}))
        self.assertTemplateUsed(response, 'blog/detail.html')

    def test_list_contains_correct_objects(self):
        response = self.client.get(reverse('blog:index'))
        self.assertContains(response, "Yesterday")
        self.assertContains(response, "Today")
        self.assertNotContains(response, "Tomorrow")
