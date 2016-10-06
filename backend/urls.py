from django.conf.urls import patterns, include, url
from django.contrib import admin
from abiz.views import ArticleListView
import debug_toolbar

urlpatterns = patterns(
    '',
    # Examples:
    # url(r'^$', 'af.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^backend/', include(admin.site.urls)),
    url(r'^admindocs/', include(
        'django.contrib.admindocs.urls', namespace='admindocs')),
    url(r'^a/', include('abiz.urls', namespace='article')),
    url(r'^__debug__/', include(debug_toolbar.urls)),
    url(r'^(?P<page>\d{0,11})$', ArticleListView.as_view(), ),
    url(r'^storage/', include('storage.urls', namespace='storage')),
    # url(r'^accounts/', include('registration.backends.default.urls')),
)
