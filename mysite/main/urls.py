from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views

urlpatterns = [
                  path('', views.Homepage.as_view(), name="homepage"),
                  path('news/', views.NewsListView.as_view(), name="news"),
                  path(r'news/<slug>/', views.NewsDetail.as_view(), name="news-detail"),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
