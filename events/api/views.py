from rest_framework.generics import ListAPIView

import datetime

from ..models import Event
from .serializers import EventSerializer


class EventListAPIView(ListAPIView):
    serializer_class = EventSerializer

    def get_queryset(self):
        return Event.objects.filter(date__gte=datetime.date.today())
