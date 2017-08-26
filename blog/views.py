from django.views.generic import ListView, DetailView

# from braces.views import CanonicalSlugDetailMixin

from .models import Blog


# Create your views here.
class BlogListView(ListView):
    model = Blog
    ordering = '-pub_datetime'
    template_name = 'blog/index.html'

    def get_queryset(self):
        return Blog.published.all()

    def get_context_data(self, **kwargs):
        context = super(BlogListView, self).get_context_data(**kwargs)
        context['blog_active'] = True
        return context


# class BlogDetailView(CanonicalSlugDetailMixin, DetailView):
class BlogDetailView(DetailView):
    model = Blog
    template_name = 'blog/detail.html'

    def get_queryset(self):
        return Blog.published.all()

    def get_context_data(self, **kwargs):
        context = super(BlogDetailView, self).get_context_data(**kwargs)
        context['blog_active'] = True
        return context
