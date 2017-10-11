from rest_framework import serializers

from ..models import Event, Venue


class VenueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Venue
        fields = ('name', 'location', 'url')


class EventSerializer(serializers.ModelSerializer):
    venue = VenueSerializer()

    class Meta:
        model = Event
        fields = ('venue', 'date', 'ticket_url', 'info')
