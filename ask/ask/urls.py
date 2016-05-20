from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ask.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'ask.views.test', name='test'),
    url(r'^login/', 'ask.views.test', name='test'),
    url(r'^signup/', 'ask.views.test', name='test'),
    url(r'^ask/', 'ask.views.test', name='test'),
    url(r'^popular/', 'ask.views.test', name='test'),
    url(r'^new/', 'ask.views.test', name='test'),
    url(r'^question/(\d+)/', 'ask.views.test', name='test'),
)
