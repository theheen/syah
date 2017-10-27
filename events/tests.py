import datetime

from django.test import TestCase
from django.urls import reverse

from .models import Event, Venue

# Create your tests here.


class EventModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        wembley = Venue.objects.create(
            name="Wembley Stadium", location="London, UK")
        Event.objects.create(
            venue=wembley, date=datetime.date.today(), info="today")

    def test_event_str(self):
        event = Event.objects.get(info="today")
        # expected = '%s: %s' % (event.date, event.venue.name)
        # expected = ''.join([str(datetime.date.today()), ': Wembley Stadium'])
        expected = '{0}: {1}'.format(event.date, event.venue.name)
        self.assertEqual(str(event), expected)

    def test_venue_str(self):
        venue = Venue.objects.get(name="Wembley Stadium")
        self.assertEqual(str(venue), "Wembley Stadium")


class EventViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        wembley = Venue.objects.create(
            name="Wembley Stadium", location="London, UK")
        Event.objects.create(
            venue=wembley, date=datetime.date.today(), info="today")
        Event.objects.create(
            venue=wembley,
            date=(datetime.date.today() + datetime.timedelta(days=1)),
            info="tomorrow")
        Event.objects.create(
            venue=wembley,
            date=datetime.date.today() - datetime.timedelta(days=1),
            info="yesterday")

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/events/')
        self.assertEqual(response.status_code, 200)

    def test_view_accessible_by_name(self):
        response = self.client.get(reverse('events:index'))
        self.assertEqual(response.status_code, 200)

    def test_events_active_context(self):
        response = self.client.get(reverse('events:index'))
        self.assertTrue('events_active' in response.context)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('events:index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'events/index.html')

    def test_date_filter(self):
        response = self.client.get(reverse('events:index'))
        self.assertContains(response, "today")
        self.assertContains(response, "tomorrow")
        self.assertNotContains(response, "yesterday")


class EventAPITest(TestCase):
    @classmethod
    def setUpTestData(cls):
        wembley = Venue.objects.create(
            name="Wembley Stadium", location="London, UK")
        Event.objects.create(
            venue=wembley, date=datetime.date.today(), info="today")
        Event.objects.create(
            venue=wembley,
            date=datetime.date.today() - datetime.timedelta(days=1),
            info="yesterday")

    def test_list(self):
        response = self.client.get(
                reverse('api:events'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "today")
        self.assertNotContains(response, "yesterday")
