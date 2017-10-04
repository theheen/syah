from django.views.generic import ListView
from rest_framework.generics import ListAPIView

import datetime

from .models import Event
from .serializers import EventSerializer


# Create your views here.
class EventListView(ListView):
    model = Event
    ordering = 'date'
    template_name = 'events/index.html'
    queryset = Event.objects.filter(date__gte=datetime.date.today())

    def get_context_data(self, **kwargs):
        context = super(EventListView, self).get_context_data(**kwargs)
        context['events_active'] = True
        return context


class EventAPIListView(ListAPIView):
    serializer_class = EventSerializer

    def get_queryset(self):
        return Event.objects.filter(date__gte=datetime.date.today())
