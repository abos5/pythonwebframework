from django.conf.urls import patterns, url
from storage import views


urlpatterns = patterns(
    '',
    url(r'^upload/$', views.upload, name='upload'),
    # url(r'^view/$', views.upload, name='upload'),
)
