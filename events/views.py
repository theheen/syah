from django.views.generic import ListView

import datetime

from .models import Event


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
