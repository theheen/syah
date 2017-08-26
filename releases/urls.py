from django.conf.urls import url

from . import views

app_name = 'releases'
urlpatterns = [
    url(r'^$', views.ReleaseListView.as_view(), name='index'),
    url(
        # r'^(?P<pk>[0-9]+)-(?P<slug>[-_\w\d]+)/$',
        # r'^(?P<pk>[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12})-(?P<slug>[-_\w\d]+)/$',
        r'^(?P<slug>[-_\w\d]+)/$',
        views.ReleaseDetailView.as_view(),
        name='detail')
]
