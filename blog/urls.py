from django.conf.urls import url

from . import views

app_name = 'blog'
urlpatterns = [
    url(r'^$', views.BlogListView.as_view(), name='index'),
    url(
        # r'^(?P<pk>[0-9]+)-(?P<slug>[-\w]+)/$',
        r'^(?P<slug>[-_\w\d]+)/$',
        views.BlogDetailView.as_view(),
        name='detail')
]
