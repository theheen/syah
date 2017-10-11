from rest_framework import serializers
from ..models import Blog


class BlogSerializer(serializers.HyperlinkedModelSerializer):
    # url = serializers.HyperlinkedIdentityField(
    #     view_name='blog-api', lookup_field='slug')

    class Meta:
        model = Blog
        fields = ('url', 'title', 'text', 'pub_datetime')
        extra_kwargs = {
            'url': {
                'view_name': 'api:blog-detail',
                'lookup_field': 'slug'
            }
        }
