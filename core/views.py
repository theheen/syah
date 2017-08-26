# from django.shortcuts import render
from django.views.generic import DetailView

from releases.models import Release

# Create your views here.


class HomepageView(DetailView):
    model = Release
    template_name = 'homepage.html'

    def get_object(self):
        return Release.published.filter(
            pub_datetime__isnull=False).latest('pub_datetime')
