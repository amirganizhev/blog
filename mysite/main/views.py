from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import News_pages


class Homepage(TemplateView):
    template_name = "main/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        return self.render_to_response(context)


class NewsListView(ListView):
    template_name = "main/news.html"
    model = News_pages

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context

# class News(DetailView):
#     template_name = "main/news.html"
#     model = News_pages
#
#     def get_context_data(self, **kwargs):
#         context = super(News).get_context_data(**kwargs)
#         context['body']=self.model.objects.filter(name=self.get_object())
#         return context
