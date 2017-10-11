from rest_framework.viewsets import ReadOnlyModelViewSet

from ..models import Release
from .serializers import ReleaseSerializer


class ReleaseReadOnlyViewset(ReadOnlyModelViewSet):
    model = Release
    serializer_class = ReleaseSerializer
    lookup_field = 'slug'

    def get_queryset(self):
        return Release.published.order_by('-release_date')
