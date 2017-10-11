from rest_framework.viewsets import ReadOnlyModelViewSet

from ..models import Blog
from .serializers import BlogSerializer


class BlogReadOnlyViewset(ReadOnlyModelViewSet):
    model = Blog
    serializer_class = BlogSerializer
    lookup_field = 'slug'

    def get_queryset(self):
        return Blog.published.all()
