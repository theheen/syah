from django.conf.urls import url, include

from rest_framework import routers

from events.api import views as event_views
from blog.api import viewsets as blog_views
from releases.api import viewsets as release_views

router = routers.SimpleRouter()
router.register(r'blog', blog_views.BlogReadOnlyViewset, base_name='blog')
router.register(
    r'releases', release_views.ReleaseReadOnlyViewset, base_name='release')

urlpatterns = [
    url(
        regex=r'^events/$',
        view=event_views.EventListAPIView.as_view(),
        name='events'),
    url(r'^', include(router.urls)),
    # url(
    #     regex=r'^blog/$',
    #     view=blog_views.BlogAPIReadOnlyViewset.as_view({
    #         'get': 'list'
    #     }),
    #     name='blog'),
]
