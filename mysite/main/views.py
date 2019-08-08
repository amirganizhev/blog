from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from .models import NewsPages


class Homepage(TemplateView):
    template_name = "main/index.html"

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        return self.render_to_response(context)


class NewsListView(ListView):
    template_name = "main/news.html"
    model = NewsPages


class NewsDetail(DetailView):
    template_name = "main/news.html"
    model = NewsPages
    slug_field = 'name'
