import datetime

from django.test import TestCase
from django.utils import timezone

from blog.models import Blog


# Create your tests here.
class BlogModelTests(TestCase):
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

    def test_is_published_property(self):
        bl_yesterday = Blog.objects.get(title="Yesterday")
        bl_today = Blog.objects.get(title="Today")
        bl_tomorrow = Blog.objects.get(title="Tomorrow")
        self.assertTrue(bl_yesterday.is_published)
        self.assertTrue(bl_today.is_published)
        self.assertFalse(bl_tomorrow.is_published)

    def test_str(self):
        bl = Blog.objects.get(title="Yesterday")
        self.assertEqual(str(bl), "Yesterday")

    def test_absolute_url(self):
        bl = Blog.objects.get(title="Yesterday")
        expected = '/blog/yesterday/'
        self.assertEqual(bl.get_absolute_url(), expected)
