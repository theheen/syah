from rest_framework.serializers import HyperlinkedModelSerializer

from ..models import Release, Track


class TrackSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Track
        fields = ('title', 'length')


class ReleaseSerializer(HyperlinkedModelSerializer):
    tracks = TrackSerializer(many=True, read_only=True, source='track_set')

    class Meta:
        model = Release
        fields = ('url', 'title', 'release_date', 'tracks', 'tagline', 'info',
                  'release_type', 'cover')
        extra_kwargs = {
            'url': {
                'view_name': 'api:release-detail',
                'lookup_field': 'slug'
            }
        }
