from django.urls import path
from . import views

urlpatterns = [
    path('', views.Homepage.as_view(), name="homepage"),
    path('news/', views.NewsListView.as_view(), name="news"),
    path(r'news/<slug>', views.NewsListView.as_view(), name="news-detail"),

]
