from django.views.generic import ListView, DetailView

from .models import Release


class ReleaseListView(ListView):
    model = Release
    # ordering = '-release_date'
    template_name = 'releases/index.html'

    def get_queryset(self):
        return Release.published.order_by('-release_date')

    def get_context_data(self, **kwargs):
        context = super(ReleaseListView, self).get_context_data(**kwargs)
        context['releases_active'] = True
        return context


class ReleaseDetailView(DetailView):
    model = Release
    template_name = 'releases/detail.html'

    def get_queryset(self):
        return Release.published.prefetch_related('track_set', 'link_set')

    def get_context_data(self, **kwargs):
        context = super(ReleaseDetailView, self).get_context_data(**kwargs)
        context['releases_active'] = True
        return context
