from django.conf.urls import url

from . import views

app_name = 'events'
urlpatterns = [
    url(r'^$', views.EventListView.as_view(), name='index'),
    # url(r'(?P<pk>[0-9]+)/$', views.EventDetailView.as_view(), name='detail'),
]
