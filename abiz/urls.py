from django.conf.urls import patterns, url
from abiz import views


urlpatterns = patterns(
    '',
    url(r'^l/(?P<page>\d{0,11})$', views.ArticleListView.as_view(), name='list'),
    url(r'^(?P<pk>\d{0,11})$', views.ArticleDetailView.as_view(), name='detail'),
    url(r'^HelloWorld$', views.HelloWorld)
)
